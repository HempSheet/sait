from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really long secret key'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = '???@gmail.com'  # адрес электронной почты здесь для отправки
app.config['MAIL_DEFAULT_SENDER'] = '???@gmail.com'  # и здесь для отправки
app.config['MAIL_PASSWORD'] = 'pass'  # пароль почти


app.config.update()
mail = Mail(app)

if __name__ == "__main__":

    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["???@gmail.com"],  # адрес электронной почты здесь для получения
                      body="This is a test email I sent with Gmail!!!")
        mail.send(msg)
