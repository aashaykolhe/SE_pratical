import random
import senders__data as Get
import smtplib
import unittest


class generate_otp(unittest.TestCase):
    # Getting Login credentials from sender_data file
    Sender_Mail = Get.email
    PassWord = Get.password

    def __init__(self, receivers_name, receivers_email, n):
        self.receivers_name = receivers_name
        self.receivers_email = receivers_email
        self.n = n
        OTP = self.create_otp(self.n)

        # testing for otps length
        self.assertBetween(self.n, 4, 8)

        # validating emailid
        self.validation()

        self.send_email(OTP)

    def create_otp(self, n):
        self.n = n
        OTP = ""
        for i in range(self.n):
            OTP += str(random.randint(0, 9))
        return (OTP)

    def __str__(self):
        return ('{} has {} as an email'.format(self.receivers_name, self.receivers_email))

    def assertBetween(self, n, low, hi):
        if not (low <= n <= hi):
            raise AssertionError('Length of OTP is %r should be in between %r and %r' % (n, low, hi))
        print("------------------------------------------------------------")

    def validation(self):
        email = "aashaykolhe2628@gmail.com"
        check_email = ("@" and "gmail" and "." and "com") in email  # self.receivers_email
        if check_email:
            print("No error in email")
        else:
            self.assertTrue(check_email)

    def send_email(self, OTP):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.Sender_Mail, self.PassWord)

        msg = ('Hi {}\n {} is your otp'.format(self.receivers_name, self.create_otp(self.n)))
        print(msg)
        server.sendmail(self.Sender_Mail, self.receivers_email, msg)
        server.quit()
        print("Email is sent!")

g = generate_otp('Aashay', 'aashaykolhe1@gmail.com', 4)
