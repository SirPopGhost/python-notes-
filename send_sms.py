from twilio.rest import Client
import os 

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=os.getenv('FROM'),
  body='This is a message from Srikar using twilio. Hello daddy, I am using an api to send a sms message to you. Enjoy your trip.',
  to=os.getenv('TO'),
)

print(message.sid)