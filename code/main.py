import flask as fl
from flask_sqlalchemy import SQLAlchemy
import os
import controller as con
from database import db_session
import database
import models as ml
import flask_login as flog
import datetime


app = fl.Flask(__name__)
lm = flog.LoginManager() # initialise the login lib
lm.init_app(app) # init the login
app.secret_key = database.get_env_variable("SECRET_KEY")  # Change this!
app.permanent_session_lifetime = datetime.timedelta(hours=12)

# below defines the mapping between URI -> controller code
@app.route('/')
def index():
    return con.index()

@app.route('/index')
def redirect_index():
    return con.index()

# send /login traffic the login page.
@app.route('/login', methods=['GET', 'POST'])
def login():
    return con.login()

@app.route('/create', methods=['GET', 'POST'])
def create():
    return con.create_account()

@app.route('/confirm_account/<int:id>')
@flog.login_required
def confirm_account(id):
    return con.confirm_account(id)

@app.route('/logged-in')
@flog.login_required
def logged_in():
    return "This is a page for those who have logged in!"

@app.route("/logout")
@flog.login_required
def logout():
    fl.session.clear()
    flog.logout_user()
    return fl.redirect(fl.url_for('index'))

@app.route("/manage")
@flog.login_required
def manage():
    return con.manage_profile()

@app.route("/edit-user/<int:id>", methods=['GET', 'POST'])
@flog.login_required
def edit_user(id):
    return con.edit_user(id)

@app.route('/delete-user/<int:id>')
def delete_user(id):
    return con.delete_user(id)

@lm.user_loader
def load_user(user_id):
    user = ml.User.query.get(user_id)
    if user:
        return user
    else:
        return None

# tear down the session iff the app shuts down
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
