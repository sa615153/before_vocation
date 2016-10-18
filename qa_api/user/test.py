from qa_api.models import User
from flask_wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form

form=model_form(User,Form)
print form.password
print dir(form)

