#-*- coding: utf-8 -*-                                                                                  

'''                                                                                                     
                                                                                                        
author: PauMB                                                                                           
Program: Send a simple mail                                                                             
Date: 08/09/14                                                                                          
Company: HedaSoft                                                                                       
                                                                                                        
'''

#importing libreries                                                                                    

import smtplib
from email.mime.text import MIMEText

#data mail                                                                                              
From = 'paumb85@gmail.com'
To = 'paumb85@gmail.com'
Subject = 'Prueba Mail'
Text = 'Contenido del mail a enviar'

def envioMail(sendFrom,sendTo,sendSubject,sendText):
    # Creamos el mensaje                                                                                
    msg = MIMEText(sendText)

    # data mail                                                                                         
    msg['Subject'] = sendSubject
    msg['From'] = sendTo
    msg['To'] = sendTo

    # Connect awith server                                                                              
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login("YourMail","Your_Password")
    # send mail                                                                                         
    mailServer.sendmail(sendFrom, sendTo, msg.as_string())
    # Close                                                                                             
    mailServer.close()

envioMail(From,To,Subject,Text)
