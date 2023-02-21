from flask import *
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sing in')


application = Flask(__name__)
application.config['SECRET_KEY'] = 'i-could-cry-for-a-smile-could-die-for-a-gun'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-could-cry-for-a-smile-could-die-for-a-gun'


application.config.from_object(Config)


@application.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        print(form.username.data, form.password.data)
        return redirect('/index')
    return render_template('registr.html', title='Sign In', form=form)


if __name__ == '__main__':  # Создаем точку доступа
    application.run(debug=False)  # Запускаем приложение без опции дебага
