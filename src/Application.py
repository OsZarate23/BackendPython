from flask import Flask
from src.controller.UserController import user_blueprint
from src.interceptors.Interceptors import FlaskInterceptors

app = Flask(__name__)
app.register_blueprint(user_blueprint)

app.errorhandler(400)(FlaskInterceptors.handle_400_error)
app.errorhandler(404)(FlaskInterceptors.handle_404_error)
app.errorhandler(500)(FlaskInterceptors.handle_500_error)

if __name__ == '__main__':
    app.run(debug=True)
