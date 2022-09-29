import re
from tkinter import Y
import stdiomask
import pandas as pd
import smtplib
import random
from email.message import EmailMessage


# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
userdatabasedict={}

def is_valid_name(s):
    return all(char.isalpha() or char.isspace() for char in s)

def is_valid_password(s):
    return bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', s))

def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False

def emailing(emailingsubject, emailingmessage):

    msg = EmailMessage()
    msg.set_content(emailingmessage)

    msg['Subject'] = emailingsubject
    msg['From'] = "no.reply.ticketreservationportal@gmail.com"
    msg['To'] = "adilahmed986@gmail.com"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("no.reply.ticketreservationportal@gmail.com", "ticketreservationportal")
    server.send_message(msg)
    server.quit()
    # # create smtp session
    # s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
    # #    start TLS for E-mail security
    # s.starttls()
    # # Log in to your gmail account
    # s.login("no.reply.ticketreservationportal@gmail.com", "ticketreservationportal")
    
    # # email = no.reply.ticketreservationportal@gmail.com
    # # password = ticketreservationportal

    # s.sendmail("no.reply.ticketreservationportal@gmail.com", "adilahmed986@gmail.com", emailingmessage)
    # # close smtp session
    # s.quit()

def register():
    name = "143"
    while not is_valid_name(name):
        name = input("Enter your name:- ")
        if is_valid_name(name):
            email = "?"
            while not check(email):
                email = input("Enter your Email ID:- ")
                userdatabase = pd.read_csv("UserDatabase.csv", on_bad_lines='skip')
                num = 0
                checkemail = False
                for r in userdatabase.Email_ID:
                    if r != email:
                        num = num+1;
                        checkemail = False
                    else:
                        checkemail = True
                        break
                if check(email) and checkemail == False:
                    password = "abc"
                    confirmpassword="cde"
                    while (password != confirmpassword):
                        while not is_valid_password(password):
                            password = stdiomask.getpass("Enter your password (Atleast one number and one alphabet should be present):- ")
                            if is_valid_password(password):
                                confirmpassword = stdiomask.getpass("Please re-enter your password:- ")
                                if password == confirmpassword:
                                    print("Please wait...")
                                    otp = random.randint(100000, 999999)
                                    otp = str(otp)
                                    emailingsubject = "OTP for account activation on TicketReservationPortal"
                                    emailingmessage = "\n Dear " + name + "," + "\n\n\n Please enter this OTP to activate your account: \n\n\t\t\t" + otp + "\n\n\n Thank you for using our service. \n\n\n\n\n\n Please note, none of these channels ask for any confidential information such as OTP, credit/debit card, CVV, Pin, Password etc, do not share these details with anyone over the phone, chat, SMS or email. \n\n\n\n Regards, \n Team Stark."
                                    emailing(emailingsubject, emailingmessage)
                                    enteredotp = 1
                                    while(enteredotp != otp):
                                        enteredotp = input("Please enter the OTP sent to your email address to activate this account:- ")
                                        if enteredotp == otp:
                                            print("Your account has been created successfully.")
                                            global userdatabasedict
                                            userdatabasedict = {'Name': [name], 'Email_ID': [email], 'Password': [password]}
                                            dsuserdatabase = pd.DataFrame(userdatabasedict)
                                            dsuserdatabase.to_csv('UserDatabase.csv', mode='a', index=False, header=False)
                                        else:
                                            print("The OTP you entered is incorrect!!")
                                else:
                                    print("Passwords do not match! Please try again!")
                            else:
                                print("\n\n\t\t\t ------------Invalid Password!!-------------- \n\t -------- Atleast one number and one alphabet should be present!!---------- \n\t\t---------No Special Characters Allowed!!!--------------- \n\n")
                elif check(email) and checkemail == True:
                    print("Email already registered!")
                    forget_password_prompt = input(" To recover password, Press P \n To login, Press L \n To return to Main Menu, Press M")
                    forget_password_prompt = forget_password_prompt.upper()
                    # if forget_password_prompt() == 'P':
                    #     forget_password()
                    # elif forget_password_prompt() == 'L':
                    #     login()
                    # else:
                    #     menu()
                else:
                    print("Please Enter a Valid Email ID!!")
        else:
            print("Please Enter a Valid Name")
    # userdatabase = pd.read_csv('UserDatabase.csv')

def login():
    email = input ("Enter your Email ID:- ")
    userdatabase = pd.read_csv("UserDatabase.csv", on_bad_lines='skip')
    num = 0
    checkemail = False
    for r in userdatabase.Email_ID:
        if r != email:
            num = num+1;
            checkemail = False
        else:
            checkemail = True
            break
    password = stdiomask.getpass("Enter your Password:- ")
    if checkemail == True:
        if password == userdatabase.iat[num,2]:
            checkpass = True
        else:
            checkpass = False
        if checkpass == True:
            print("Login Successful!")
    if checkemail == False or checkpass == False:
        print("Email ID or Password is incorrect!!")
        prompt = input(" To recover password, Press P \n To re-enter login details, Press L \n To return to Main Menu, Press M")
        prompt = prompt.upper()
        # if prompt == "P":
        #     forget_password()
        # elif prompt() == 'L':
        #     login()
        # # else:
        #     # menu()


def forget_password():
    email = input ("Enter your Email ID:- ")
    userdatabase = pd.read_csv("UserDatabase.csv", on_bad_lines='skip')
    num = 0
    checkemail = False
    for r in userdatabase.Email_ID:
        if r != email:
            num = num+1;
            checkemail = False
        else:
            checkemail = True
            break
    if checkemail == True:
        name = userdatabase.iat[num,0]
        print("Please wait...")
        otp = random.randint(100000, 999999)
        otp = str(otp)
        emailingsubject = "OTP for changing password on TicketReservationPortal"
        emailingmessage = "\n Dear " + name + "," + "\n\n\n Please enter this OTP to change your Password: \n\n\t\t\t" + otp + "\n\n\n Thank you for using our service. \n\n\n\n\n\n Please note, none of these channels ask for any confidential information such as OTP, credit/debit card, CVV, Pin, Password etc, do not share these details with anyone over the phone, chat, SMS or email. \n\n\n\n Regards, \n Team Stark."
        emailing(emailingsubject, emailingmessage)
        enteredotp = 1
        while(enteredotp != otp):
            enteredotp = input("Please enter the OTP sent to your email to verify it's " + name + ":- ")
            if enteredotp == otp:
                newpassword = "abc"
                confirmnewpassword="cde"
                while (newpassword != confirmnewpassword):
                    while not is_valid_password(newpassword):
                        newpassword = stdiomask.getpass("Enter your new password (Atleast one number and one alphabet should be present):- ")
                        if is_valid_password(newpassword):
                            confirmnewpassword = stdiomask.getpass("Please re-enter your new password:- ")
                            if newpassword == confirmnewpassword:
                                print("Password changed successfully!")
                                userdatabase.drop(userdatabase.index[num], inplace=True)
                                userdatabase.to_csv("UserDatabase.csv", index=False, sep=',')
                                global userdatabasedict
                                userdatabasedict = {'Name': [name], 'Email_ID': [email], 'Password': [newpassword]}
                                dsuserdatabase = pd.DataFrame(userdatabasedict)
                                dsuserdatabase.to_csv('UserDatabase.csv', mode='a', index=False, header=False)
                                # menu()
    else:
        print("No such user exists!")
        prompt = ("Do you want to create a new account?(Y/N):- ")
        prompt = prompt.upper()
        if prompt == 'Y':
            register()
        else:
            print("Menu")
            # menu()
    

# register()
# login()
forget_password()