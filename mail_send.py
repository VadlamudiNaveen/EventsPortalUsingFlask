from app import app, mongo
from flask_mail import Mail, Message

mail = Mail(app)
temp = list(mongo.db.users.find())
with app.app_context():
    with mail.connect() as conn:
        for user in temp:
            print(user['name'])
            message = 'Hello everyone how are you i hope every one are fine and thop.. happy UGADI...'
            subject = "hello, %s" % 'naveen'
            msg = Message(recipients=['jufyitepsa@enayu.com'], body=message, subject=subject)
            conn.send(msg)
        print("done sending the mails")
