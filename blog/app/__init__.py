from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
admin = Admin(app, name='microblog', template_mode='bootstrap3')
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views
