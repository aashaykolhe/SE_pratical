import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('aashaykolhe2628@gmail.com',password="cmnm gnqw xcca nqkb")
otp = random.randrange(100000, 1000000)
message = "OTP for logon is "+str(otp)
server.sendmail('aashaykolhe2628@gmail.com','aashaykolhe1@gmail.com',message)
server.quit()
user = int(input("Enter the OTP: "))
if(user == otp):
    print("access granted")
else:
    print("access denied")