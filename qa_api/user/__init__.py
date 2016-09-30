from flask import Blueprint

user = Blueprint(
    'user',
    __name__,
    template_folder='./templates',
    static_folder='./static',
    url_prefix='/user'
)

from . import views