#!/usr/bin/python

import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase

email_user = 'petmanagerclr@gmail.com'
email_send = 'petmanagerclr@gmail.com'
subject= 'Phyton!'

msg = MIMEMultipart()
msg ['From'] = email_user
msg ['To'] = email_user
msg ['Subject'] = subject

body = 'Hola , este es un mail de phyton'
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'petman20191')

server.sendmail(email_user,email_send,text)
server.quit()
