#!/usr/bin/python

import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email import encoders
import time

def load_file(file, file_name):
    read_file = open(file,'rb')
    attach = MIMEBase('multipart', 'encrypted')
    attach.set_payload(read_file.read()) 
    read_file.close()  
    encoders.encode_base64(attach) 
    attach.add_header('Content-Disposition', 'attachment', filename=file_name)
    return attach

def sendemail(addr_to_mail, ruta):
    smtp_server = 'smtp.gmail.com:587'
    smtp_user   = 'petmanagerclr@gmail.com'
    smtp_pass   = 'petman2019'
    fecha=str(time.strftime("%d-%m-%y"))
    email = MIMEMultipart() 
    email['To'] = addr_to_mail
    email['From'] = 'petmanagerclr@gmail.com'
    email['Subject'] = 'Reporte PETManager'
    email.attach(MIMEText('<p style="color:red;" >Envio Archivo Reporte PET Manager</p>','html'))
    email.attach(load_file(ruta,fecha+'.csv'))
    smtp = smtplib.SMTP(smtp_server)
    smtp.starttls()
    smtp.login(smtp_user,smtp_pass)
    smtp.sendmail(addr_from_mail, addr_to_mail, email.as_string())
    smtp.quit()
    print ("E-mail enviado!")

def sendmailini():
    mail = input("Ingrese mail destino")
    ruta = input("Ingrese ruta del archivo Ej: C:/Users//Desktop/archivo.csv")
    sendemail(mail,ruta)

sendmailini()
