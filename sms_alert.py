#YLVENQL98KJHRGJ649YHU4LT
#+18777804236



from twilio.rest import Client


account_sid = "AC3b433202f35ccc9f4dd98fe812329b3f"
auth_token = "826cb21795e9cf17b789c9c06fe0dfd2"



client = Client(account_sid, auth_token)


def message = client.messages.create(
    body="Some Stranger has arrived",
    from_="+18582408811",
    to="+918610131862",
    
)
def message1 = client.messages.create(
    body="Some Stranger has arrived",
    from_="+18582408811",
    to="+919940225157",
    
)
print(message.sid)
print(message1.sid)
