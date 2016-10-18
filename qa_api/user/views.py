#from qa_api import user
#from flask import render_template, flash, redirect, url_for, request

from database import Session
from flask import render_template, jsonify,flash,redirect,url_for,request
import pdb
from wtforms import BooleanField,StringField
from ..forms import UserAddTaskForm, UserLoginForm, UserSignUpForm,TestForm1,TestForm2,AddIARForm,AddIDEASForm
from ..models import MajorTask,SubTask,User,SubtaskProperty
from . import user
import time
#add on 10.10am by jpang3
from flask_login import login_user, logout_user, current_user,login_required


def create_user_add_task_form(isideas,session):
    basic_form = UserAddTaskForm()
    print type(basic_form)
    subtask_list=session.query(SubtaskProperty).filter(SubtaskProperty.task_category == isideas).all()
    subdict = {}
    for subtask in subtask_list:
        subtask_name = subtask.subtask_name
        print "subname:"+ subtask_name
        subdict[subtask_name]=BooleanField(subtask_name,default=False)
        UserAddTaskForm.subtask_name = BooleanField(subtask_name,default=False)

    UserAddTaskForm.subtask_dict = subdict
    subtask_name = subtask_list[0].subtask_name
    UserAddTaskForm.subtask_name = BooleanField(subtask_name, default=False)



    print basic_form.gitDir
    print type(basic_form.gitDir)
    print '**********************'
    subtask = subtask_list[0]
    subtask_name = subtask.subtask_name
    print StringField(subtask_name, default=False)
    UserAddTaskForm.tmp = BooleanField(subtask_name,default=False)
    print "add done"
    print "UserAddTaskForm.gitDir"
    print UserAddTaskForm.gitDir
    print "type"
    print type(UserAddTaskForm.gitDir)
    print "UserAddTaskForm.tmp"
    print UserAddTaskForm.tmp
    print "type"
    print type(UserAddTaskForm.tmp)
    #
    newins = UserAddTaskForm()

    # print type(StringField(subtask_name,default=False))
    print '-------------- create done -------------'

    # basic_form.subtask_dict=subdict

    # print basic_form.subtask_dict[subtask_list[0].subtask_name]
    return newins



@user.route('/test', methods=['GET', 'POST'])
def test():
    form1 = TestForm1()
    form2 = TestForm2()
    if form1.validate_on_submit():# and form2.validate_on_submit():
        input1_data = form1.input1.data
        input2_data = request.form.get('input2')

        print "print_input1_data:::by form1.input1.data::::   " + input1_data
        print "print_input2_data:::by request.form.get('input2')::::   " + input2_data
        #127.0.0.1 - - [13/Oct/2016 17:33:32] "GET /user/test HTTP/1.1" 200 -
        #print_input1_data:::by form1.input1.data::::   f1 i1
        #print_input2_data:::by request.form.get('input2')::::   f1 i2
        #127.0.0.1 - - [13/Oct/2016 17:33:51] "POST /user/test HTTP/1.1" 200 -


        #out_input1test = form1.out_input1.data
        #AttributeError: 'TestForm1' object has no attribute 'out_input1'

        out_input1 = request.form.get('out_input1')
        print "print_out_input1_data:::by request.form.get('out_input1')::::   "
        print out_input1

        out_input2 = request.form.get('input2name')
        print "print_out_input1_data:::by request.form.get('out_input2name')::::   "
        print out_input2

        #127.0.0.1 - - [13/Oct/2016 17:50:53] "POST /user/test HTTP/1.1" 200 -
        #print_input1_data:::by form1.input1.data::::   f1i1
        #print_input2_data:::by request.form.get('input2')::::   f1i2

        #print_out_input1_data:::by request.form.get('out_input1')::::
        #None
        #print_out_input1_data:::by request.form.get('out_input2')::::
        #oi2


        f2_input3_data = form2.input3.data
        print "print_f2_input3_data:::by form2.input3.data::::   " + f2_input3_data
        f2_input4_data = request.form.get('input4')
        print "print_f2_input3_data:::by form2.input3.data::::   " + f2_input4_data

        # with out if form2.validate, only form1.validate can make program here
        #print_f2_input3_data:::by form2.input3.data::::   f2i3
        #print_f2_input3_data:::by form2.input3.data::::   f2i4
        #
        #




    return render_template('test.html', form1=form1,form2=form2)


@user.route('/newtask',methods = ['GET', 'POST'])
def add_new_task():
    # userAddTaskform = UserAddTaskForm()
    # if userAddTaskform.validate_on_submit():
    #     session = Session()
    #     #pdb.set_trace()
    #     newMajorTask = MajorTask(track_number = 'test-forms',status = '0',account = 'qa',begin_time='201609180907',is_test2 = '0',is_ideas = '0',saved_tag = '',comments = '',git_dir = userAddTaskform.gitDir.data)
    #     session.add(newMajorTask)
    #     session.commit()
    #     session.close()
    #     return "insert success!"
    task_category = request.args['category']
    name = request.args['username']
    print("%s",task_category)
    print("%s",name)

    session = Session()
    new_task_form = create_user_add_task_form(task_category,session)
    #if new_task_form.validate_on_submit():

    print "@start"
    print "------UserAddTaskForm.tmp   UserAddTaskForm.subtask_name----"
    print UserAddTaskForm.tmp
    print UserAddTaskForm.subtask_name
    print "type"
    print type(UserAddTaskForm.tmp)
    print type(UserAddTaskForm.subtask_name)

    print "@"
    print "------new_task_form.tmp   new_task_form.subtask_name----"
    print new_task_form.tmp
    print new_task_form.subtask_name
    print "type"
    print type(new_task_form.tmp)
    print type(new_task_form.subtask_name)

    print "-----UserAddTaskForm.subtask_dict--------"
    print UserAddTaskForm.subtask_dict
    print "type"
    print type(UserAddTaskForm.subtask_dict)
    print "dict[0]"
    print type(UserAddTaskForm.subtask_dict['checkgui_linux'])
    print "-----new_task_form.subtask_dict--------"
    print new_task_form.subtask_dict
    print "type"
    print type(new_task_form.subtask_dict)
    print "dict[0]"
    print type(new_task_form.subtask_dict['checkgui_linux'])

    new_task_form.ins_attr = BooleanField("ins_proper", default=False)
    print "******ins_new_attr*******"
    print new_task_form.ins_attr
    print "type"
    print type(new_task_form.ins_attr)



    return render_template('newtask.html', form=new_task_form, name='pangy')

@user.route('/login',methods = ['GET','POST'])
def login():
    userLoginForm = UserLoginForm()
    print("userLoginForm :%s",userLoginForm.userName.data)
    print("userLoginForm :%s", userLoginForm.passWord.data)
    print("userLoginForm :validate_on_submit", userLoginForm.validate_on_submit())

    if userLoginForm.validate_on_submit():
        print("validate")
        session = Session()
        username = session.query(User).filter(User.user_name == userLoginForm.userName.data).first()
        if username is None:
            flash(u'Username or Password is not correct')
            return render_template('login.html', form=userLoginForm)

        if username is not None and username.password==userLoginForm.passWord.data:
            #remvove comment on 10.10 by jpang3
            login_user(username)
            session.commit()
            name = current_user.user_name
            session.close()
            print url_for('user.index', username="1")
            return redirect(url_for('user.index', username=name)) #pass
        else:
            print("password wrong")
            flash(u'Username or Password is not correct')
            return render_template('login.html',form=userLoginForm)
    return render_template('login.html',form=userLoginForm)

@user.route('/index/<username>',methods = ['GET','POST'])
def index(username):
    return render_template('index.html', name=username)


#add on 10.10 by jpang3
@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@user.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserSignUpForm()

    if form.validate_on_submit():
        session = Session()
        signup_name = form.userName.data
        signup_password = form.passWord.data
        test = session.query(User).filter(User.user_name == signup_name).first()

        if test:  # user_name exists
            flash('username: ' + signup_name + ' exists, change a new one')
            session.commit()
            session.close()
            return render_template('signup.html', form=form)

        else:  # signup_name is a new name
            new_user = User()
            new_user.user_name = signup_name
            new_user.password = signup_password
            session.add(new_user)
            session.commit()

            login_user(new_user)

            session.close()
            return redirect(url_for('user.AddNewTask'))

    return render_template('signup.html', form=form)


time_stamp_format = '%Y%m%d%H%M%S'
@user.route('/addideas',methods = ['GET', 'POST'])
def addideas():
    form = AddIDEASForm()
    print "1"
    if form.validate_on_submit():
        print "2"
        new_task=MajorTask()
        current_time = time.strftime(time_stamp_format)
        current_user = request.args['username']
        tracknumber = 'IDEAS-'+current_time+"-"+current_user+"-"+form.title.data
        new_task.account = current_user
        new_task.track_number = tracknumber
        new_task.status = 0
        new_task.git_dir = form.gitDir.data
        new_task.begin_time = current_time
        new_task.is_test2 = 0
        new_task.is_ideas = 0
        new_task.saved_tag =''
        new_task.comments = form.comments.data
        new_task.backup_path = ''

        #add to database
        session = Session()
        session.add(new_task)
        session.commit()

        subtask_name_list = ['check_autocase', 'checkcode_quality', 'check_compile_win_intel', 'check_compile_win_vc',
                             'check_dependency', 'check_iar_lib', 'check_ideas_lib', 'check_linux_compile', 'check_performance',
                             'check_sc', 'checkgui_linux', 'checkgui_win']


        for subtask_name in subtask_name_list:
            if request.form.get(subtask_name)=='y':
                new_subtask = SubTask()
                new_subtask.name = subtask_name
                new_subtask.major_task_track_number = tracknumber
                new_subtask.status = 0
                new_subtask.benchmark = request.form.get('benchmark')

                session.add(new_subtask)
                session.commit()
        session.close()
        return redirect(url_for('user.index', username=current_user))

    return render_template('addideas.html', form=form)



@user.route('/addiar', methods=['GET', 'POST'])
def addiar():
    form = AddIARForm()
    if form.validate_on_submit():
        pass

    return render_template('addiar.html', form=form)

