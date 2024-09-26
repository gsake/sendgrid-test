import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Instructions 
# Step 1:
# Update the MAIL_FROM, MAIL_TO and SENDGRID_API_KEY
#
# Step 2: 
# python sendSendgridEmail_SMTP.py


# Email Sender / Receiver
MAIL_FROM = 'NoReply <noreply@sendgrid_verified_domain.net>'
MAIL_TO = 'George Sakellaris <georgios.sakellaris@gmail.com>'

msg = MIMEMultipart()
msg['From'] = MAIL_FROM
msg['To'] = MAIL_TO
msg['Subject'] = 'Sending mails from SMTP'
mail_body = """
Hey,

This is a test.

Regards,\nRuan

"""
msg.attach(MIMEText(mail_body))

try:
    server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
    server.ehlo()

    SENDGRID_API_KEY='SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    server.login('apikey', SENDGRID_API_KEY)

    server.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
    server.close()
    print("mail sent")
except smtplib.SMTPException as e:
    print(e)
