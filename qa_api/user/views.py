#from qa_api import user
#from flask import render_template, flash, redirect, url_for, request

from database import Session
from flask import render_template, jsonify
from flask_login import login_user

import pdb

from ..forms import UserAddTaskForm, UserLoginForm
from ..models import MajorTask,SubTask,User
from . import user

@user.route('/newtask',methods = ['GET', 'POST'])
def AddNewTask():
    userAddTaskform = UserAddTaskForm()
    if userAddTaskform.validate_on_submit():
        session = Session()
        #pdb.set_trace()
        newMajorTask = MajorTask(track_number = 'test-forms',status = '0',account = 'qa',begin_time='201609180907',is_test2 = '0',is_ideas = '0',saved_tag = '',comments = '',git_dir = useractionform.gitDir.data)
        session.add(newMajorTask)
        session.commit()
        session.close()
        return "insert success!"
    return render_template('newtask.html',form=userAddTaskform,name='pangy')

@user.route('/login',methods = ['GET','POST'])
def Loginin():
    userLoginForm = UserLoginForm()
    print("userLoginForm :%s",userLoginForm.userName.data)
    if userLoginForm.validate_on_submit():
        print("validate")
        session = Session()
        user = session.query.filter_by(username=userLoginForm.userName).first()
        if user is not None and user.verify_password(userLoginForm.passWord.data):
            login_user(user)
            return "user exists!" #pass
    return render_template('login.html',form=userLoginForm)

@user.route('/',methods = ['GET','POST'])
def index():
    return "Hello"



