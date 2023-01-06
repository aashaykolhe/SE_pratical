# SEND MAIL FROM SENDER TO RECEIVER MAIL

import random
import smtplib  #number of digits of OTP

def get_email():
    n=int(input("Enter value of number of digits to generate OTP: "))
def GENERATE_OTP():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('aashaykolhe2628@gamil.com',password='cmnm gnqw xcca nqkb')
    otp=''.join([str(random.randint(0,9))for i in range(n)])
    msg='Hello, your otp is '+str(otp)
    server.sendmail('aashaykolhe2628@gmail.com','aashaykolhe1@gmail.com',msg)
 
    server.quit()
    print(otp)
get_email()
GENERATE_OTP()



