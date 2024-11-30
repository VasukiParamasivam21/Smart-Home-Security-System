import smtplib
from email.message import EmailMessage
from twilio.rest import Client

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to'] =to
    msg['from']="ramya.devtest.mail@gmail.com"
    user="ramya.devtest.mail@gmail.com"
    password="wjgfyarvwubrpuss"

    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

if __name__== '__main__':
    email_alert("testmail","this is test mail","ramyaravi654@gmail.com")

def sms_alert():
    account_sid = "AC3b433202f35ccc9f4dd98fe812329b3f"
    auth_token = "826cb21795e9cf17b789c9c06fe0dfd2"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Some Stranger has arrived",
        from_="+18582408811",
        to="+918610131862",
    
    )
    message1 = client.messages.create(
        body="Some Stranger has arrived",
        from_="+18582408811",
        to="+917397125015",
    
    )
    message1 = client.messages.create(
        body="Some Stranger has arrived",
        from_="+18582408811",
        to="+918110093177",
    
    )
    message1 = client.messages.create(
        body="Some Stranger has arrived",
        from_="+18582408811",
        to="+918838400247",
    
    )


