from flask import Flask
from . import dispatcher
from . import PC
from . import user

app = Flask(__name__)
app.config['SECRET_KEY']='secret_key_here'
app.config.from_object('apiconfig')
# blueprint here?(flask-restful) or user/dispatcher/PC/(flask-website)     for now user/dispatcher/PC/


app.register_blueprint(dispatcher.mod)
app.register_blueprint(PC.mod)
app.register_blueprint(user.user)
