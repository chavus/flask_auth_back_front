import os, socket
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'secretkey'

port = int(os.environ.get("PORT"))
print('port : ', port)
host = socket.gethostname()
print('host :', host)
auth_api_url = "http://" + host + ":" + str(port)


db = SQLAlchemy(app)
Migrate(app, db)


from flask_restful import Api
from auth_api.resources.user import UserRegister, UserAuth, User
from auth_api.resources.item import Item, ItemList

api = Api(app)

api.add_resource(Item, '/api/item/<string:name>')
api.add_resource(ItemList, '/api/items')
api.add_resource(UserRegister, '/api/register')
api.add_resource(UserAuth, '/api/auth')
api.add_resource(User, '/api/user')


login_manager.init_app(app)
login_manager.login_view = 'users.login'

from auth_api.core_front.views import core_blueprint
from auth_api.users_front.views import users_blueprint


app.register_blueprint(core_blueprint)
app.register_blueprint(users_blueprint)
