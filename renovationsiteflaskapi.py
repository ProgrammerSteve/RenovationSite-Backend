from flask import Flask, redirect, url_for, request,jsonify
from flask_mail import Mail,  Message
from flask_cors import CORS
from dotenv import dotenv_values

envDict = dotenv_values(".env")
app = Flask(__name__)
CORS(app)

mail_settings={
    "MAIL_SERVER":'smtp.gmail.com',
    "MAIL_PORT":465,
    "MAIL_USE_TLS":False,
    "MAIL_USE_SSL":True,
    "MAIL_USERNAME" : envDict['MAILUSER'],
    "MAIL_PASSWORD" : envDict['MAILPW']}
app.config.update(mail_settings)
mail = Mail(app)

@app.route('/',methods = ['POST','GET'])
def index():
    name=''
    tel=''
    email=''
    textArea=''
    if request.method == 'POST':
        appform = request.get_json( )
        name = appform['name']
        tel = appform['tel']
        email = appform['email']
        textArea = appform['textArea']
    if request.method == 'GET' or 'POST':
        with app.app_context():
            msg=Message(
                subject='Zaya Renovations Quote Request:',
                sender=envDict['MAILUSER'],
                recipients=[envDict['MAILREC']],
                body="name: %s\n tel: %s\n email: %s\n text: %s"%(name,tel,email,textArea))
            mail.send(msg)
            return jsonify('Email Sent')

if __name__ == '__main__':
    app.run()

