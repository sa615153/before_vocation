#from qa_api import user
#from flask import render_template, flash, redirect, url_for, request

from database import Session
from flask import render_template, jsonify,flash,redirect,url_for
import pdb

from ..forms import UserAddTaskForm, UserLoginForm
from ..models import MajorTask,SubTask,User
from . import user

#add on 10.10am by jpang3
from flask_login import login_user, logout_user, current_user,login_required


@user.route('/test',methods = ['GET', 'POST'])
def test():
    flash('hello hello how are you')
    return "hello"




@user.route('/newtask',methods = ['GET', 'POST'])
def AddNewTask():
    userAddTaskform = UserAddTaskForm()
    if userAddTaskform.validate_on_submit():
        session = Session()
        #pdb.set_trace()
        newMajorTask = MajorTask(track_number = 'test-forms',status = '0',account = 'qa',begin_time='201609180907',is_test2 = '0',is_ideas = '0',saved_tag = '',comments = '',git_dir = userAddTaskform.gitDir.data)
        session.add(newMajorTask)
        session.commit()
        session.close()
        return "insert success!"
    return render_template('newtask.html',form=userAddTaskform,name='pangy')

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
            session.close()
            return redirect(url_for('user.AddNewTask')) #pass
        else:
            print("password wrong")
            flash(u'Username or Password is not correct')
            return render_template('login.html',form=userLoginForm)
    return render_template('login.html',form=userLoginForm)

@user.route('index',methods = ['GET','POST'])
def index():
    return "Hello"


#add on 10.10 by jpang3
@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))
