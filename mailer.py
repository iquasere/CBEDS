from flask import Flask, json, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = 'maildosequeira@gmail.com',
    MAIL_PASSWORD = 'yjxqbcivcykfghtn'
)

mail = Mail(app)

@app.route('/mailer', methods=['POST'])
def send_mail():
    jeison = request.get_json()
    print(jeison)
    #{'name': 'João Sequeira', 'email': 'maildosequeira@gmail.com', 'subject': 'UniProt ID mapping API inconsistent', 'message': 'text\n\nText'}
    msg = Message(jeison['message'],
                  sender=jeison['email'], 
                  recipients=["cbedsymposium@gmail.com"])
    mail.send(msg)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run()