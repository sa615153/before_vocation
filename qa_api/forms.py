from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField,BooleanField
from qa_api.models import  Machine, MajorTask, SubTask, SubtaskProperty
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class UserAddTaskForm(FlaskForm):

    gitDir = StringField(u'gitDir', validators=[DataRequired(), Length(max=15)])

    submit = SubmitField(u'submit')


    #subtask_dict = subdict#
    #{   : bolleanfield  ,   :  bolleanfield ,   : bolleanfield  }

    #html
    #form.subtask_dict
    #form.subtask_dict.k



class UserLoginForm(FlaskForm):
    userName = StringField(u'username', validators=[DataRequired(), Length(max=50)])
    passWord = PasswordField(u'password', validators=[DataRequired()])
    submit = SubmitField(u'login')


class UserSignUpForm(FlaskForm):

    userName = StringField('user name', validators=[DataRequired(), Length(max=50)])
    passWord = PasswordField('password', validators=[DataRequired()])
    confirm_passWord = PasswordField('password', validators=[DataRequired(), EqualTo('passWord', message='not equal')])
    submit = SubmitField('sign___up')


class AddIDEASForm(FlaskForm):
    gitDir = StringField(u'gitDir', validators=[DataRequired(), Length(max=15)])
    title = StringField(u'title',validators=[DataRequired(), Length(max=100)])
    comments = StringField(u'comments',validators=[DataRequired(), Length(max=300)])
    #fix fields, remain to be altered dynamic
    checkgui_win = BooleanField(u'check GUI in Win',default=False)
    checkgui_linux = BooleanField(u'check GUI in Linux', default=False)
    check_code_quality = BooleanField(u'check code quality',default=False)
    check_autocase = BooleanField(u'check Autocase',default=False)
    check_compile_win_intel = BooleanField(u'check compile in Win with Intel',default=False)
    check_compile_win_vc = BooleanField(u'check compile Win with MSVC', default=False)
    check_dependency = BooleanField(u'check Dependency',default=False)
    check_linux_compile = BooleanField(u'check compile in Linux with Intel',default=False)
    check_performance = BooleanField(u'check Performance',default=False)
    check_sc = BooleanField(u'check Share-Component',default=False)
    check_ideas_lib = BooleanField(u'Calculate IDEAS Case Library',default=False)
    check_iar_lib = BooleanField(u'Calculate IAR Case Library',default=False)

    submit = SubmitField(u'submit')


class AddIARForm(FlaskForm):
    gitDir = StringField(u'gitDir', validators=[DataRequired(), Length(max=15)])
    title = StringField(u'title', validators=[DataRequired(), Length(max=100)])
    comments = StringField(u'comments', validators=[DataRequired(), Length(max=300)])

    # fix fields, remain to be altered dynamic
    check_code_quality = BooleanField(u'check_code_quality',default=False)
    check_compile_win_intel = BooleanField(u'check_compile_win_intel',default=False)
    check_compile_win_vc = BooleanField(u"check_compile_win_vc",default=False)
    check_linux_compile = BooleanField(u'check_linux_compile',default=False)
    check_iar_lib = BooleanField(u'Calculate IAR Case Library', default=False)

    submit = SubmitField(u'submit')







#####################################################################
class addideasform():
    gitDir = StringField(u'gitDir', validators=[DataRequired(), Length(max=15)])
    title = StringField(u'title',validators=[DataRequired(), Length(max=100)])
    comments = StringField(u'comments',validators=[DataRequired(), Length(max=300)])
    #fix fields, remain to be altered dynamic
    checkgui_win = BooleanField(u'check GUI in Win',default=False)
    checkgui_linux = BooleanField(u'check GUI in Linux', default=False)
    check_code_quality = BooleanField(u'check code quality',default=False)
    check_autocase = BooleanField(u'check Autocase',default=False)
    check_compile_win_intel = BooleanField(u'check compile in Win with Intel',default=False)
    check_compile_win_vc = BooleanField(u'check compile Win with MSVC', default=False)
    check_dependency = BooleanField(u'check Dependency',default=False)
    check_linux_compile = BooleanField(u'check compile in Linux with Intel',default=False)
    check_performance = BooleanField(u'check Performance',default=False)
    check_sc = BooleanField(u'check Share-Component',default=False)
    check_ideas_lib = BooleanField(u'Calculate IDEAS Case Library',default=False)
    check_iar_lib = BooleanField(u'Calculate IAR Case Library',default=False)

    submit = SubmitField(u'submit')



if __name__ == "__main__":

    strlist = dir(addideasform)
    print strlist

    insta = addideasform()

    # for attribute in strlist:
    print getattr(addideasform,"title")
    print type(getattr(addideasform,"title"))

    print "*********"
    print getattr(insta,"title")
    print type(getattr(insta,"title"))






























########################################################################
class TestForm1(FlaskForm):
    input1 = StringField('input1', validators=[DataRequired()])
    input2 = StringField('input2dif', validators=[DataRequired()])
    submit = SubmitField('TestForm1_submit')


class TestForm2(FlaskForm):
    input3 = StringField('input3', validators=[DataRequired()])
    input4 = StringField('input4', validators=[DataRequired()])
    input5 = BooleanField('checkbox', default=False)
    submit2 = SubmitField('TestForm2_submit')
########################################################################

