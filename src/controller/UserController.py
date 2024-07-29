from flask import Blueprint, request, jsonify, Flask
from src.service import UserService

user_blueprint = Blueprint('UserController', __name__)
app = Flask(__name__)

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = UserService.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        return str(e), 500
