from flask import Blueprint, render_template, jsonify
from flask_restful import Api
from .available_task_pc_match import AvailableTaskPCMatch

mod = Blueprint('dispatcher', __name__, url_prefix='/dispatcher')

dispatcher_api = Api(mod)
dispatcher_api.add_resource(AvailableTaskPCMatch, '/AvailableTaskPCMatch',endpoint='available_task_match')

