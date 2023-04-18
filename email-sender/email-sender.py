from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'krishnachandu1998@gmail.com'
email_password = password
email_reciever = 'chandukrishna1998@gmail.com'

subject = "Sending Email Through the python"

body = """
Hello Chandu,
 We are sending you mail using the the python. We are using the email library for that. We import the smtplib library for sending the Email.
 """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
