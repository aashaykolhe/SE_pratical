import datetime
import imghdr
import mysql.connector
import os
import pywhatkit
import smtplib
import senders__data as Get
from email.message import EmailMessage

Senderemail=Get.email
SenderPassword=Get.password

now = str(datetime.date.today())
#print(now) #format of date = YYYY-MM-DD
today=now[8:10]+now[5:7]
print("Todays date "+today)  #format of birthday=DDMM

#database connection
mydb = mysql.connector.connect(host="localhost",user="root",password="mysql_password",database = "bday-data")
mycursor = mydb.cursor()


#inserting data into database
def add_data():
    mycursor1 = mydb.cursor()
    print("Enter details of person")
    name = input("Enter name:")
    birth_date = input("Enter birthdate in format datemonth like 2112 :")
    number = input("Enter mobile number :")
    email = input("Enter Email id: ")
    sql = "INSERT INTO data (name, birth_date,mobile_no,email_id ) VALUES (%s, %s, %s,%s)"
    person = (name,birth_date,number,email)
    mycursor1.execute(sql, person)
    mydb.commit()
    print("Data added!!")

#display the persons data from table
def display_data():
    display=mydb.cursor()
    display.execute("select * from data")
    person_list=display.fetchall()
    for person in person_list:
        print(person)

#method for sending whatsapp message
def send_whatsappmessage(data):
    name =data[0]
    number='+91'+data[2]
    img="D:\college b.tech\water park"
    pywhatkit.sendwhats_image(number,img,'Hi '+name+'\nMany many happy returns of the day!',15,True,3)

#method for sending image on email
def send_emailimage(data):
    with open ("birthday_img.jpg",'rb') as m:
        file_data = m.read()
        file_type = imghdr.what(m.name)
        file_name = m.name

    receiveremail=data[3]
    msg=EmailMessage()
    msg['Subject']='Sending birthday wishes'
    msg['From']=Senderemail
    msg['to']=receiveremail
    msg.set_content("Hi "+data[0]+"\n Happy Birthday")
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
    #login into senders server
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(Senderemail,SenderPassword)
    server.send_message(msg)
    print("greetings sent !")
    server.quit()

def send_emailmessage(data):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    receiveremail=data[3]
    msg='Hi'+data[0]+" \n many many happy returns of the day!"
    server.login(Senderemail,SenderPassword)
    server.sendmail(Senderemail,receiveremail,msg)
    print("email text sent ")
    server.quit()

add_data()
display_data()
mycursor.execute(f"select * from data where birth_date = {today}")
li =mycursor.fetchall()
for i in li:
    send_whatsappmessage(i)
    send_emailimage(i)
    send_emailmessage(i)
