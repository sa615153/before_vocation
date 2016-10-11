from flask import Flask

from flask_bootstrap import Bootstrap
from flask_login import LoginManager


bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'admin.login'
login_manager.login_message = u'Please sign in firstly!'


app = Flask(__name__)
bootstrap.init_app(app)
login_manager.init_app(app)
app.config['SECRET_KEY']='secret_key_here'
app.config.from_object('apiconfig')
# blueprint here?(flask-restful) or user/dispatcher/PC/(flask-website)     for now user/dispatcher/PC/

from . import dispatcher
from . import PC
from . import user
app.register_blueprint(dispatcher.mod)
app.register_blueprint(PC.mod)
app.register_blueprint(user.user)
