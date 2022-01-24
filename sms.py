from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACea0205ede8e46d9b203c9e8db549d603"
# Your Auth Token from twilio.com/console
auth_token  = "00818030dbe932ac4d73e77e8c4ad5d0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="+15018193640", 
    to="+919789829273",
    body="emergency")

print(message.sid)

