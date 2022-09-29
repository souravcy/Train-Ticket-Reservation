from PIL import Image, ImageDraw, ImageFont
import datetime
import os
from datetime import date
import pandas as pd
import re
import random
import time
from tkinter import Y
import stdiomask
import smtplib
from email.message import EmailMessage
global is_login
is_login = False
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
userdatabasedict={}

#from csv import writer
cad = 0
dict = {}
candict = {}
trian_num = 0
list = []
df = pd.read_csv("code.csv")

# def file_exists(location):
#     file_exists1 = os.path.exists(location)
#     return file_exists1

def option():
    print("\n")
    print("Do You Want to Re-Enter the value?")
    print()
    print("Press 'Y' to Re-Enter or Press 'N' to go back to the Main Menu ")
    s = input("= ")
    s=s.upper()
    print("\n\n")
    return s

class trains:
    def print_seat_availablity(ac1,ac2,ac3,sl):
        # ac1 = str(random.randint(0, 24))
        # ac2 = str(random.randint(0, 48))
        # ac3 = str(random.randint(0, 72))
        # sl = str(random.randint(0, 80))
        # for i in arr:
        #     print("No. of seats available inAC :- " + i)

        print("No. of seats available in 1AC :- " , ac1)
        print("No. of seats available in 2AC :- " , ac2)
        print("No. of seats available in 3AC :- " , ac3)
        print("No. of seats available in SL :- " , sl)


    def seat():
        seat_1ac = str(random.randint(0,24))
        seat_2ac = str(random.randint(0,48))
        seat_3ac = str(random.randint(0,72))
        seat_sl = str(random.randint(0,80))
        seat = [seat_1ac,seat_2ac,seat_3ac,seat_sl]
        return seat

    def fares():
        fare = 0
        fare_1ac = str(random.randint(3500,4500))
        fare_2ac = str(random.randint(2165,2567))
        fare_3ac = str(random.randint(1300,1800))
        fare_sl = str(random.randint(500,750))
        fares = [fare_1ac,fare_2ac,fare_3ac,fare_sl]
        return fares

    def check_availabilty(ac1,ac2,ac3,sl, ticket_num,choice):
        # if coach not in ('SL', '1AC', '2AC','3AC'):
        #     trains.print_seat_availablity(arr)
        # print(ticket_num)
        # if ac1 == 0 or ac2 == 0 or ac3 == 0 or sl == 0:
        #     return False
        # elif (ac1 >= ticket_num) or (ac2 >= ticket_num) or (ac3 >= ticket_num) or (sl >= ticket_num):
        #     return True
        # else:
        #     return False

        if choice == '1AC':
            if ac1 == 0:
                return False
            elif ticket_num <= ac1:
                return True
            else:
                return False
        elif choice == '2AC':
            if ac2 == 0:
                return False
            elif ticket_num <= ac2:
                return True
            else:
                return False
        elif choice == '3AC':
            if ac3 == 0:
                return False
            elif ticket_num <= ac3:
                return True
            else:
                return False
        elif choice == 'SL':
            if sl == 0:
                return False
            elif ticket_num <= sl:
                return True
            else:
                return False

    def book_ticket(self, seat, no_of_tickets=0):
        seat -= no_of_tickets
        return True


class acceptors:
    def accept_menu_option():
        option = input("Enter your option :- ")
        if option not in ('1', '2', '3', '4', '5', '6', '7', '0'):
            print("Please enter a valid option!")
            return acceptors.accept_menu_option()
        else:
            return int(option)

    def accept_train_number():
        train_num = 0
        check = False
        train_num = int(input("Enter the train number :- "))
        for row in df.Train_Number:
            if row == train_num:
                check = True
                break
        if check == False:
            print("Please enter a valid train number.")
            return acceptors.accept_train_number()
        else:
            return train_num

    def accept_coach():
        coach = input("Enter the coach (1AC/2AC/3AC/SL):- ")
        coach = coach.upper()
        if coach not in ('SL', '1AC', '2AC', '3AC'):
            print("Please enter coach properly.")
            return acceptors.accept_coach()
        else:
            return coach

    def accept_prompt():
        prompt = input("Confirm? (y/n) :-")
        prompt = prompt.lower()
        if prompt not in ('y', 'n'):
            print("Please enter proper choice.")
            return acceptors.accept_prompt()
        return prompt

    def accept_ticket_num():
        ticket_num = 0
        try:
            ticket_num = int(input("Enter the number of tickets :- "))
            if ticket_num < 0:
                raise ValueError
        except ValueError:
            print("Enter proper ticket number.")
            return acceptors.accept_ticket_num()
        else:
            return ticket_num

    def accept_date_of_travel():
        today = date.today()
        today_day = today.strftime("%d")
        today_month = today.strftime("%m")
        today_year = today.strftime("%Y")
        print(today, today_day, today_month, today_year)
        date_of_travel = ''
        date_of_travel = input("Enter the date of Travel (DD/MM/YYYY):- ")
        # inputdate_of_travel = input("Enter the date_of_travel in format 'dd/mm/yy' : ")

        day, month, year = date_of_travel.split('/')
        date_of_travel1 = datetime.datetime.strptime(date_of_travel, "%d/%m/%Y").date()
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if (isValidDate):
            # checking if date is in the future
            # if int(year) - today_year > 0
            #     if int(month) - today_month > 0
            #         if int(day) - today_day > 0
            if today<date_of_travel1:
                return date_of_travel
            elif today == date_of_travel1:
                print("Sorry, No tickets available for today!")
                # prompt2 = input("Do you want to view available tickets for a different date? (Y/N)")
                # prompt2 = prompt2.upper()
                prompt2 = "LMAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
                while prompt2 != 'Y' and 'N':
                    prompt2 = input("Do you want to view available tickets for a different date? (Y/N)")
                    prompt2 = prompt2.upper()
                    if prompt2 != 'Y':
                        if prompt2 != 'N':
                            print("Please enter a valid option!!!")
                        else:
                            break
                if prompt2 == 'Y':
                    return acceptors.accept_date_of_travel()
                elif prompt2 == 'N':
                    ex()

            else:
                print("Please Enter a valid date!!")
                return acceptors.accept_date_of_travel()
        else:
            print("Please Enter a valid date!!")
            return acceptors.accept_date_of_travel()


def check_pnr():
    d = pd.read_csv("PassengerData.csv")
    pr = int(input("Enter Your Valid PNR:- "))
    num = 0
    check = False
    for r in d.PNR:
        if r != pr:
            num = num+1
            check = False
        else:
            check  = True
            break

    if check == True:
        print()
        print("\t\t\t\t---------------Your Ticket----------------")
        print("Train Number:- ",int(d.iat[num,0]), "\t\t\t\t\t\t\t", "PNR:- ", str(d.iat[num,1]))
        print("Source Station:- ",d.iat[num,2],"(",d.iat[num,9],")","\t\t","Destination Station:- ",d.iat[num,3],"(",d.iat[num,10],")" )
        print("Departure Time:- ",d.iat[num,4],"\t\t\t\t\t\t","Arrival Time:- ",d.iat[num,5])
        print("Number of Seats Booked:- ",int(d.iat[num,6]),"\t\t\t\t\t","Class:- ",d.iat[num,7])
        print("Date:- ",d.iat[num,8], "\t\t\t\t\t\t\t\t", "Booking status:- ",d.iat[num,12])
        print("\t\t\t\t------------------------------------------")
        print()
        going_back_to_menu()
    else:
        print("No Booking Found!!!")
        going_back_to_menu()
        # menu()


def going_back_to_menu():
    if is_login == True:
        menu_after_login()
    else:
        menu()

def book_ticket():
    src = input("Enter Start station code:- ")
    dst = input("Enter Destination station code:- ")
    src = src.upper()
    dst = dst.upper()
    arr = df.loc[(df['Start_Code'] == src) & (df['Destination_Code']==dst)]
    l = len(arr)
    if l == 0:
        print("\n")
        print("Train not available for this Route!")
        s = option()
        if s == 'Y':
            book_ticket()
        else:
            menu_after_login()
    print(arr)
    count = 0
    choice = acceptors.accept_train_number()
    date_of_travel = acceptors.accept_date_of_travel()

    for row in df.Train_Number:
        if row != choice:
            count += 1
        else:
            break
    destination = df.iat[count,4]
    source = df.iat[count,2]
    arrival = df.iat[count,7]
    departure = df.iat[count,6]
    list = trains.seat()
    a1 = int(list[0])
    a2 = int(list[1])
    a3 = int(list[2])
    s = int(list[3])


    trains.print_seat_availablity(a1,a2,a3,s)
    coach = acceptors.accept_coach()
    ticket_num = acceptors.accept_ticket_num()

    farelist = trains.fares()
    fareac1 = int(farelist[0])
    fareac2 = int(farelist[1])
    fareac3 = int(farelist[2])
    faresl = int(farelist[3])

    if coach == '1AC':
        each = fareac1
    elif coach == '2AC':
        each = fareac2
    elif coach == '3AC':
        each = fareac3
    elif coach == 'SL':
        each = faresl

    # fare = trains.fares(coach)
    # each = fare
    fare = int(each * ticket_num)

    # storing seatmatrix
    global seatmatrix
    seatmatrix = {'Train_Number': [choice], 'Start_Station_Code': [src],'Destination_Station_Code': [dst], 'Date': [date_of_travel], '1AC': a1, '2AC': a2, '3AC': a3, 'SL': s, 'Fare_1AC': fareac1, 'Fare_2AC': fareac2, 'Fare_3AC': fareac3, 'Fare_SL': faresl}
    seatmatrixdf = pd.DataFrame(seatmatrix)
    seatmatrixdf.to_csv('SeatMatrix.csv', mode='a', index=False, header=False)


    if trains.check_availabilty(a1,a2,a3,s,ticket_num,coach):

        print("\n\n")
        print("\t\t\t\t\t--------------- Booking Preview ----------------")
        print("Train Number:- ", int(df.iat[count, 0]) )
        print("Source Station:- ", df.iat[count, 2], "(", df.iat[count, 3], ")", "\t\t", "Destination Station:- ",
              df.iat[count, 4], "(", df.iat[count, 5], ")")
        print("Departure Time:- ", df.iat[count, 6], "\t\t\t\t\t\t", "Arrival Time:- ", df.iat[count, 7])
        print("Date:- ", date_of_travel, "\t\t\t\t\t\t\t\t", "Class:- ", coach)
        print("Number of seats:- ", ticket_num)
        print()
        print("\t\t\t\t\t------------------------------------------------")
        print()

        print("\n\n")
        print("Fare per person:- ₹", each)
        print("You have to pay :- ₹", fare)


        prompt = acceptors.accept_prompt()
        if prompt == 'y':
            if choice == '1AC':
                trains.book_ticket(a1,ticket_num)
            elif choice == '2AC':
                trains.book_ticket(a2,ticket_num)
            elif choice == '3AC':
                trains.book_ticket(a3,ticket_num)
            elif choice == 'SL':
                trains.book_ticket(s,ticket_num)
            trains.book_ticket(coach, ticket_num)
            print("Booking Successful!\n\n")
            global pnr
            pnr = str(choice) + str(random.randint(10000,99999))
            print("Here's your ticket!!")
            print("Please note your PNR number :- ", pnr, "\n\n")


            train_num1 = [choice]
            pnr1 = [pnr]
            src1 = [source]
            src2 = [src]
            dst1 = [destination]
            dsc1 = [dst]
            nos1 = [ticket_num]
            arv1 = [arrival]
            dpt1 = [departure]
            coach1 = [coach]
            far = [fare]
            date_of_travel1 = [date_of_travel]
            status1 = "Confirm"
            bookdate = date.today()
            bookdate_day = bookdate.strftime("%d")
            bookdate_month = bookdate.strftime("%m")
            bookdate_year = bookdate.strftime("%Y")
            bookdate = bookdate_day + "/" + bookdate_month + "/" + bookdate_year
            # dictionary of lists
            global dict
            dict = {'Train_Number': train_num1, 'PNR': pnr1, 'Start_Station': src1, 
                    'Destination_Station': dst1,'Departure': dpt1, 'Arrival': arv1, 
                    'Number_of_Seats': nos1, 'Class': coach1,'Day': date_of_travel1 ,
                    'Start_Station_Code': src2,'Destination_Station_Code': dsc1,
                    'Fare': far, 'Booking_Status': status1, 'BookCancelDate': bookdate }
            pic(src,dst,pnr,choice,ticket_num,date_of_travel,coach,fare,arrival,departure,status1)
            #sr,ds,pn,choi,ticket_nu,dat,coa,far,art,drt
            ds = pd.DataFrame(dict)
            ds.to_csv('PassengerData.csv', mode='a', index=False, header=False)

            # delete old seatmatrix and store new seatmatrix
            n = 0
            check = False
            for r in seatmatrixdf.Train_Number:
                if r != int(choice):
                    n = n+1
                    check = False
                else:
                    check  = True
                    break
            seatmatrixdf.drop(seatmatrixdf.index[n], inplace=True)
            seatmatrixdf.to_csv("SeatMatrix.csv", index=False, sep=',')

            if coach == '1AC':
                a1 = a1 - ticket_num
            elif coach == '2AC':
                a2 = a2 - ticket_num
            elif coach == '3AC':
                a3 = a3 - ticket_num
            elif coach == 'SL':
                s = s - ticket_num
            seatmatrix = {'Train_Number': [choice], 'Start_Station_Code': [src],
                        'Destination_Station_Code': [dst], 'Date': [date_of_travel], 
                        '1AC': a1, '2AC': a2, '3AC': a3, 'SL': s, 'Fare_1AC': fareac1, 
                        'Fare_2AC': fareac2, 'Fare_3AC': fareac3, 'Fare_SL': faresl}
            seatmatrixdf = pd.DataFrame(seatmatrix)
            seatmatrixdf.to_csv('SeatMatrix.csv', mode='a', index=False, header=False)
            menu_after_login()
        else:
            print("Exiting...\n\n")
            menu_after_login()
    else:
        print(ticket_num, " tickets not available")
        menu_after_login()


def cancel_ticket():
    data = pd.read_csv("PassengerData.csv")
    pr = str(input("Enter Your Valid PNR:- "))
    n = 0
    check = False
    for r in data.PNR:
        if r != int(pr):
            n = n+1
            check = False
        else:
            check  = True
            break

    if check == False:
        print("\n\n")
        print("Invalid PNR Number!\n\n")
        s = option()
        if s == 'Y':
            cancel_ticket()
        else:
            menu_after_login()
    status1 = data.iat[n,12]
    bookdate = data.iat[n,13]       
    if status1 == "Cancelled":
        print("Ticket was already cancelled on " + bookdate)
        menu_after_login()
    else:
        prompt = acceptors.accept_prompt()
        if prompt  == 'n':
            menu_after_login()
        else:
            train_num1 = data.iat[n,0]
            pnr1 = pr
            src1 = data.iat[n,2]
            src2 = data.iat[n,9]
            dst1 = data.iat[n,3]
            dsc1 = data.iat[n,10]
            nos1 = data.iat[n,6]
            arv1 = data.iat[n,5]
            dpt1 = data.iat[n,4]
            coach1 = data.iat[n,7]
            far = data.iat[n,11]
            date_of_travel1 = data.iat[n,8]
            # status1 = data.iat[n,12]
            # bookdate = data.iat[n,13]
            # if status1 == "Cancelled":
            #     print("Ticket was already cancelled on " + bookdate)
            #     menu_after_login()
            # else:
            print("\n\n\t\t\t\t--------------- Ticket Cancelled ----------------")
            print("\n\n\nYour amount of ₹", data.iat[n, 11], "has been refunded\n\n\n\n")
            status1 = "Cancelled"
            bookdate = date.today()
            bookdate_day = bookdate.strftime("%d")
            bookdate_month = bookdate.strftime("%m")
            bookdate_year = bookdate.strftime("%Y")
            bookdate = bookdate_day + "/" + bookdate_month + "/" + bookdate_year
            # dictionary of lists
            global candict
            candict = {'Train_Number': train_num1, 'PNR': pnr1, 'Start_Station': src1, 'Destination_Station': dst1,
                'Departure': dpt1, 'Arrival': arv1, 'Number_of_Seats': nos1, 'Class': coach1, 'Day': date_of_travel1,
                'Start_Station_Code': src2, 'Destination_Station_Code': dsc1, 'Fare': far, 'Booking_Status': status1, 'BookCancelDate': bookdate}
            # pic(src2, dsc1, pr, train_num1, nos1, date_of_travel1, coach1, far, arv1, dpt1)
            pic(data.iat[n,9], data.iat[n,10], pr, data.iat[n,0], data.iat[n,6], data.iat[n,8], data.iat[n,7], data.iat[n,11], data.iat[n,5], data.iat[n,4], status1)
            # str(data.iat[n, 1])
            # delete row
            data.drop(data.index[n], inplace=True)
            data.to_csv("PassengerData.csv", index=False, sep=',')

            # sr,ds,pn,choi,ticket_nu,dat,coa,far,art,drt
            dcancel = pd.DataFrame(candict, index=[0])
            dcancel.to_csv('PassengerData.csv', mode='a', index=False, header=False)

            seatmatrixdf = pd.read_csv("SeatMatrix.csv")
            # delete old seatmatrix and store new seatmatrix
            number = 0
            check = False
            # choice = data.iat[number,0]
            for r in seatmatrixdf.Train_Number:
                if r != int(train_num1):
                    number = number+1
                    check = False
                else:
                    check  = True
                    break
            
            # coach = data.iat[n,7]
            a1 = int(seatmatrixdf.iat[number,4])
            a2 = int(seatmatrixdf.iat[number,5])
            a3 = int(seatmatrixdf.iat[number,6])
            sleeper = int(seatmatrixdf.iat[number,7])
            # ticket_num = data.iat[n,6]
            fareac1 = int(seatmatrixdf.iat[number,8])
            fareac2 = int(seatmatrixdf.iat[number,9])
            fareac3 = int(seatmatrixdf.iat[number,10])
            faresl = int(seatmatrixdf.iat[number,11])
            seatmatrixdf.drop(seatmatrixdf.index[number], inplace=True)
            seatmatrixdf.to_csv("SeatMatrix.csv", index=False, sep=',')

            if coach1 == '1AC':
                a1 = a1 + nos1
            elif coach1 == '2AC':
                a2 = a2 + nos1
            elif coach1 == '3AC':
                a3 = a3 + nos1
            elif coach1 == 'SL':
                sleeper = sleeper + nos1
            seatmatrix = {'Train_Number': train_num1, 'Start_Station_Code': src2,
                        'Destination_Station_Code': dsc1, 'Date': date_of_travel1, 
                        '1AC': a1, '2AC': a2, '3AC': a3, 'SL': sleeper, 'Fare_1AC': fareac1, 
                        'Fare_2AC': fareac2, 'Fare_3AC': fareac3, 'Fare_SL': faresl}
            seatmatrixdf = pd.DataFrame(seatmatrix)
            seatmatrixdf.to_csv('SeatMatrix.csv', mode='a', index=False, header=False)
            menu_after_login()


def ex():
    print(
        "------------------------------------------------Thank You!-----------------------------------------------------------------------")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    exit()


def menu():
    is_login = False
    print("Choose one of the following option:-")
    print("1.Book Ticket")
    print("2.Check PNR")
    print("3.Cancel Ticket ")
    print("4.Login")
    print("5.Create account")
    print("6.Forgot Password")
    print("0.Exit")
    func = {1: temp_menu, 3: temp_menu, 4: login, 5: register, 6: forget_password, 0: ex}
    option = acceptors.accept_menu_option()
    func[option]()

def temp_menu():
    is_login = False
    print("Please login to use this feature!")
    print("Choose one of the following option:-")
    print("1.Login")
    print("2.Create account")
    print("3.Forgot Password")
    print("0.Exit") 
    func = {1: login, 2: register, 3: forget_password, 0: ex}
    option = acceptors.accept_menu_option()
    func[option]()   

def welcome_before_loginmenu(name):
    print("\t\t\t Welcome " + name)
    menu_after_login()

def menu_after_login():
    is_login = True
    print("\n\nChoose one of the following option:-")
    print("1.Book Ticket")
    print("2.Check PNR")
    print("3.Cancel Ticket ")
    print("4.Change Password")
    print("5:Logout")
    print("0.Exit")
    func = {1: book_ticket, 2: check_pnr, 3: cancel_ticket, 4: change_password, 5:logout, 0: ex}
    option = acceptors.accept_menu_option()
    func[option]() 

def pic(sr,ds,pn,choi,ticket_nu,dat,coa,far,art,drt, book_stats):

    # Variable Assignment sr,ds,pn,choi,ticket_nu,dat,coa,far,art,drt
    gnrt_date_of_travel = dat
    gnrt_train_num = str(choi)
    gnrt_class = str(coa)
    gnrt_fare = "Rs." + str(far)
    gnrt_numberpass = str(ticket_nu)
    gnrt_pnr = pn
    gnrt_d_time = drt
    gnrt_a_time = art
    gnrt_from = sr + " --- "
    gnrt_to = ds
    gnrt_from_to = gnrt_from + gnrt_to
    booking_status = book_stats
    # selecting background image depending on booking/cancelling
    if booking_status=="Confirm":
        image = Image.open('TicketBackground.png')
    else:
        image = Image.open('CancelledTicketBackground.png')
    # initialise the drawing context with
    # the image object as background
    draw = ImageDraw.Draw(image)

    rbt = ImageFont.truetype('Roboto-Bold.ttf', size=10)
    rbtsml = ImageFont.truetype('Roboto-Bold.ttf', size=9)
    tpwr = ImageFont.truetype('JMH Typewriter-Bold.ttf', size=30)
    tpwrmed = ImageFont.truetype('JMH Typewriter-Bold.ttf', size=20)
    tpwrsml = ImageFont.truetype('JMH Typewriter-Bold.ttf', size=13)

    # From-To

    (x, y) = (60, 100)
    message = "From -- To"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    (x, y) = (430, 100)
    message = "From - To"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    # Depart time

    (x, y) = (60, 158)
    message = "Departure Time:"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)


    # Arrival time

    (x, y) = (245, 158)
    message = "Arrival Time:"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)


    # date_of_travel

    (x, y) = (60, 180)
    message = "date_of_travel"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    (x, y) = (430, 150)
    message = "date_of_travel"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    # Class

    (x, y) = (195, 180)
    message = "Class"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    (x, y) = (430, 200)
    message = "Class"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    # PNR Number

    (x, y) = (310, 180)
    message = "PNR Number"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    (x, y) = (510, 200)
    message = "PNR"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    # No. of Passengers

    (x, y) = (60, 241)
    message = "Seats  Booked"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    (x, y) = (430, 250)
    message = "Seats"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    # TrainNumber

    (x, y) = (195, 241)
    message = "Train No."
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    (x, y) = (500, 250)
    message = "Train No."
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)


    # Fare

    (x, y) = (314, 241)
    message = "Fare"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)


    # From-To
    (x, y) = (48, 111)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_from_to, fill=color, font=tpwr)
    (x, y) = (428, 117)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_from_to, fill=color, font=tpwrsml)

    # date_of_travel
    (x, y) = (55, 193)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_date_of_travel, fill=color, font=tpwrmed)
    (x, y) = (428, 165)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_date_of_travel, fill=color, font=tpwrsml)

    # Class
    (x, y) = (193, 193)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_class, fill=color, font=tpwrmed)
    (x, y) = (428, 215)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_class, fill=color, font=tpwrsml)

    # PNR
    (x, y) = (298, 193)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_pnr, fill=color, font=tpwrmed)
    (x, y) = (498, 215)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_pnr, fill=color, font=tpwrsml)

    # No. of seats
    (x, y) = (63, 255)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_numberpass, fill=color, font=tpwrmed)
    (x, y) = (435, 265)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_numberpass, fill=color, font=tpwrsml)

    # Train no.
    (x, y) = (190, 255)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_train_num, fill=color, font=tpwrmed)
    (x, y) = (504, 265)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_train_num, fill=color, font=tpwrsml)

    # Fare
    (x, y) = (310, 255)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_fare, fill=color, font=tpwrmed)

    # Departtime
    (x, y) = (150, 156)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_d_time, fill=color, font=tpwrsml)
    (x, y) = (503, 165)
    gnrt_dat_time = "at " + gnrt_d_time
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_dat_time, fill=color, font=tpwrsml)

    # Arrival time
    (x, y) = (315, 156)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_a_time, fill=color, font=tpwrsml)

    image.show()

    file_name = gnrt_pnr + ".png"
    # #delete previous file with same name
    # file_exists = os.path.exists("D:\\Programming\\TicketReservationPortalSystem\\Tickets\\"+file_name)
    # if file_exists == True:
    #     os.remove("D:\\Programming\\TicketReservationPortalSystem\\Tickets\\"+file_name)
    # save the edited image
    image.save("D:\\Programming\\TicketReservationPortalSystem\\Tickets\\"+file_name)
    


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
    # server.send_message(msg)
    server.quit()
    print (msg)

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
                                            welcome_before_loginmenu(name)
                                        else:
                                            print("The OTP you entered is incorrect!!")
                                else:
                                    print("Passwords do not match! Please try again!")
                            else:
                                print("\n\n\t\t\t ------------Invalid Password!!-------------- \n\t -------- Atleast one number and one alphabet should be present!!---------- \n\t\t---------No Special Characters Allowed!!!--------------- \n\n")
                elif check(email) and checkemail == True:
                    print("Email already registered!\n")
                    forget_password_prompt = input("To recover password, Press P \n To login, Press L \n To return to Main Menu, Press M\n")
                    forget_password_prompt = forget_password_prompt.upper()
                    if forget_password_prompt() == 'P':
                        forget_password()
                    elif forget_password_prompt() == 'L':
                        login()
                    else:
                        menu()
                else:
                    print("Please Enter a Valid Email ID!!")
        else:
            print("Please Enter a Valid Name")

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
            name = userdatabase.iat[num,0]
            welcome_before_loginmenu(name)
    if checkemail == False or checkpass == False:
        print("Email ID or Password is incorrect!!")
        prompt = input(" To recover password, Press P \n To re-enter login details, Press L \n To return to Main Menu, Press M")
        prompt = prompt.upper()
        if prompt == "P":
            forget_password()
        elif prompt() == 'L':
            login()
        else:
            menu()


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
                                print("Password changed successfully!\n\n")
                                userdatabase.drop(userdatabase.index[num], inplace=True)
                                userdatabase.to_csv("UserDatabase.csv", index=False, sep=',')
                                global userdatabasedict
                                userdatabasedict = {'Name': [name], 'Email_ID': [email], 'Password': [newpassword]}
                                dsuserdatabase = pd.DataFrame(userdatabasedict)
                                dsuserdatabase.to_csv('UserDatabase.csv', mode='a', index=False, header=False)
                                welcome_before_loginmenu(name)
    else:
        print("No such user exists!")
        prompt = ("Do you want to create a new account?(Y/N):- ")
        prompt = prompt.upper()
        if prompt == 'Y':
            register()
        else:
            menu()

def change_password():
    print("Change Password feature coming soon!")
    menu()

def logout():
    print("Logout feature coming soon!")
    menu()

menu()

exit()

# pnr check can't detect if logged in or logged out