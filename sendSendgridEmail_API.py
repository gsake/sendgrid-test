# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python


# Instructions 
# Step 1:
# Update the MAIL_FROM, MAIL_TO and SENDGRID_API_KEY
#
# Step 2: 
# echo "export SENDGRID_API_KEY='SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'" > sendgrid.env
# source ./sendgrid.env
#
# Step 3: 
# python sendSendgridEmail_API.py


import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

MAIL_FROM='yyy@yyy.yyy'
MAIL_TO='xxx@xxx.xxx'

message = Mail(
    # from_email='noreply@circuit.com',
    from_email=MAIL_FROM,
    to_emails=MAIL_TO,
    subject='Sending mails from API',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)