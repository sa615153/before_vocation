# -*- coding: utf-8 -*-

from database import Session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

from qa_api.models import MajorTask
from qa_api.models import Machine
from qa_api.models import SubTask
from qa_api.models import SubtaskProperty
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy import or_



import time


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)
parser.add_argument('tracknumber', type=str)
parser.add_argument('status', type=str)




class AvailableTaskPCMatch(Resource):
    def check_precondition_status(self,subtask):

        precondition = subtask.property.precondition

        if precondition == 'no':
            return True
        for isubtask in subtask.MajorTask.subtasks:
            if isubtask.name == precondition and isubtask.status == 2 and isubtask.result == 'success':
                return True
            else:
                return False

    def get(self):
        # 创建独立session,为互斥使用,贯彻整个get
        session = Session()

        # 将来要返回给dispatcher的初始“任务-机器”对 列表
        return_list = []

        ############################################
        ###lock using table machine
        ############################################

        # find idle machines
        idle_machine_list = session.query(Machine).with_lockmode('update').filter(Machine.status == '0').all()

        # print (idle_machine_list)
        # find conclusion report type subtasks in subtask table
        conclusion_report_list = session.query(SubTask).filter(SubTask.name == 'report').all()
        # print "123"
        # filter to figure out all windows machines to do report in idle machine list
        available_doreport_machine_list = filter(lambda x: True if x.label == 'windows' else False, idle_machine_list)

        # assign reports to idle windows machines
        for ival in range(0, len(conclusion_report_list) - 1):
            if ival < len(available_doreport_machine_list):
                return_list.append((conclusion_report_list[ival], available_doreport_machine_list[ival]))
                # remove target machine cos it has been assigned to do report
                idle_machine_list.remove(available_doreport_machine_list[ival])
                # end of report subtask assginment

        # find to do subtasks
        todo_list = session.query(SubTask).filter(SubTask.status == 0).filter(SubTask.name != 'report').all()

        # no_report_todo_list = filter(lambda x: True if x.name == "report" else False,todo_list)
        # filter machine label list
        machine_label_list = set([])
        for machine in idle_machine_list:
            machine_label_list.add(machine.label)
        # contains machines in each label, such as {linux:[machine1,machine2],windows:[machine3,machin4]}
        idle_machine_dict = {}
        for machine_label in machine_label_list:
            buf_list = filter(lambda x: True if x.label == machine_label else False, idle_machine_list)
            idle_machine_dict[machine_label] = buf_list
        # print idle_machine_dict

        priority_list = [0, 1, 2]

        for machine_label in machine_label_list:
            for priority in priority_list:
                flag = 'nobreak'
                target_subtask_list = filter(
                    lambda x: True if x.property.label == machine_label and x.MajorTask.is_test2 == priority else False,
                    todo_list)
                target_subtask_list = filter(self.check_precondition_status, target_subtask_list)
                print ("second layer for     label:", machine_label, "priority:", priority)
                print "target subtasks"
                print(target_subtask_list)
                print "machines of this label"
                print idle_machine_dict[machine_label]

                # distribute subtasks to machines
                # 问题是过早改掉了machinelist，　需在第三层内部machinelist保持不变，第三层ｆｏｒ结束后，维护machinelist，


                # bug fix
                assigned_machine_list = ([])
                print "before third for"

                for ival in range(0, len(target_subtask_list)):
                    machine_length = len(idle_machine_dict[machine_label])
                    if ival < machine_length:
                        print ('length:target_subtask_list------', len(target_subtask_list))
                        print ('length:idle_machine_dict[machine_label]------', len(idle_machine_dict[machine_label]))
                        print ("ival: ", ival)
                        print "---------------------------------------------------------------------------------------------------------------------------------"
                        print ("assign ", target_subtask_list[ival], " to ", idle_machine_dict[machine_label][ival])
                        print "--------------------------------------assign end--------------------------------------------------"
                        return_list.append((target_subtask_list[ival], idle_machine_dict[machine_label][ival]))
                        # bug fix cancel this
                        # idle_machine_dict[machine_label].remove(idle_machine_dict[machine_label][ival])

                        # bug fix
                        assigned_machine_list.append(idle_machine_dict[machine_label][ival])


                    else:  # run out machines of this label, need to jump out this assign for and outer priority for to continue next label
                        flag = 'break'
                        print ("break  ival=", ival)
                        print "run out machines of this label"
                        print "after this second for, the return_list is :"
                        print return_list
                        break
                # bug fix : maintain machines of this label
                for i in assigned_machine_list:
                    idle_machine_dict[machine_label].remove(i)

                if flag == 'break':
                    break
        print "********************************************"
        # print return_list
        return_dict = {}
        for t in return_list:
            return_dict[t[1].IP] = t[0]
        print return_dict

        session.commit()
        return return_dict





