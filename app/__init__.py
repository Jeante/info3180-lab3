from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'f665f68ae95da7'
app.config['MAIL_PASSWORD'] = '434a5abdfe63d9'
mail = Mail(app)
from app import views