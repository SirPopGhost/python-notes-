#  https://github.com/conventional-changelog/commitlint
#   https://www.twilio.com/en-us/sendgrid/email-api 
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email= os.getenv('FROM_EMAIL'),
    to_emails=os.getenv('TO_EMAIL'),
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)

