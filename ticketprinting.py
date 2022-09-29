from PIL import Image, ImageDraw, ImageFont
import datetime
import pandas as pd
import re
import random
#from csv import writer
dict = {}
trian_num = 0
list = []
df = pd.read_csv("code.csv")


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
        seat = [str(random.randint(0, 24)),str(random.randint(0, 48)),str(random.randint(0, 72)),str(random.randint(0, 80))]
        return seat

    def fares(choice):
        fare = 0
        if choice == '1AC':
            fare = str(random.randint(3500,4500))
        elif choice == '2AC':
            fare = str(random.randint(2165,2567))
        elif choice == '3AC':
            fare = str(random.randint(1300,1800))
        elif choice == 'SL':
            fare = str(random.randint(500,750))
        return int(fare)

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

    def accept_date():
        date = ''
        date = input("Enter the Date of Travel (DD/MM/YYYY):- ")
        # inputDate = input("Enter the date in format 'dd/mm/yy' : ")

        day, month, year = date.split('/')

        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if (isValidDate):
            return date
        else:
            print("Please Enter a valid Date!!")
            return acceptors.accept_date()


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
        print("Train Number:- ",int(d.iat[num,0]))
        print("Source Station:- ",d.iat[num,2],"(",d.iat[num,9],")","\t\t","Destination Station:- ",d.iat[num,3],"(",d.iat[num,10],")" )
        print("Departure Time:- ",d.iat[num,4],"\t\t\t\t\t\t","Arrival Time:- ",d.iat[num,5])
        print("Number of Seats Booked:- ",int(d.iat[num,6]),"\t\t\t\t\t","Class:- ",d.iat[num,7])
        print("Date:- ",d.iat[num,8])
        print("\t\t\t\t------------------------------------------")
        print()
        menu()
    else:
        print("No Booking Found!!!")
        menu()


def book_ticket():
    src = input("Enter Start station code:- ")
    dst = input("Enter Destination station code:- ")
    src = src.upper()
    dst = dst.upper()
    arr = df.loc[(df['Start_Code'] == src) & (df['Destination_Code']==dst)]
    print(arr)
    count= 0
    choice = acceptors.accept_train_number()
    date = acceptors.accept_date()

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


    if trains.check_availabilty(a1,a2,a3,s,ticket_num,coach):
        fare = trains.fares(coach)
        fare = int(fare * ticket_num)
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
            date1 = [date]
            # dictionary of lists
            global dict
            dict = {'Train_Number': train_num1, 'PNR': pnr1, 'Start_Station': src1, 'Destination_Station': dst1,
                    'Departure': dpt1, 'Arrival': arv1, 'Number_of_Seats': nos1, 'Class': coach1,'Day': date1 ,
                    'Start_Station_Code': src2,'Destination_Station_Code': dsc1,'Fare': far }
            pic(src,dst,pnr,choice,ticket_num,date,coach,fare,arrival,departure)
            #sr,ds,pn,choi,ticket_nu,dat,coa,far,art,drt
            ds = pd.DataFrame(dict)
            ds.to_csv('PassengerData.csv', mode='a', index=False, header=False)

            menu()
        else:
            print("Exiting...\n\n")
            menu()
    else:
        print(ticket_num, " tickets not available")
        menu()


def cancel_ticket():
    data = pd.read_csv("PassengerData.csv")
    pr = int(input("Enter Your Valid PNR:- "))
    n = 0
    check = False
    for r in data.PNR:
        if r != pr:
            n = n+1
            check = False
        else:
            check  = True
            break
    print(n)

    data.drop(data.index[n], inplace=True)
    data.to_csv("PassengerData.csv", index=False, sep=',')
    print("\t\t\t\t--------------- Ticket Cancelled ----------------")
    menu()


def ex():
    print(
        "------------------------------------------------Thank You!-----------------------------------------------------------------------")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    exit()


def menu():
    print("Choose one of the following option:-")
    print("1.Book Ticket")
    print("2.Cancel Ticket")
    print("3.Check PNR ")
    print("0.Exit")
    func = {1: book_ticket, 2: cancel_ticket, 3: check_pnr, 0: ex}
    option = acceptors.accept_menu_option()
    func[option]()


def pic(sr,ds,pn,choi,ticket_nu,dat,coa,far,art,drt):

    # create Image object with the input image

    image = Image.open('TicketBackground.png')

    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)

    # create font object with the font file and specify
    # desired size

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


    # Date

    (x, y) = (60, 180)
    message = "Date"
    color = 'rgb(150, 150, 150)'  # grey color
    draw.text((x, y), message, fill=color, font=rbt)

    (x, y) = (430, 150)
    message = "Date"
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

    # Variable Assignment sr,ds,pn,choi,ticket_nu,dat,coa,far,art,drt
    gnrt_date = dat
    gnrt_train_num = str(choi)
    gnrt_class = str(coa)
    gnrt_fare = "Rs."+str(far)
    gnrt_numberpass = str(ticket_nu)
    gnrt_pnr = pn
    gnrt_d_time = drt
    gnrt_a_time = art
    gnrt_from = sr+" --- "
    gnrt_to = ds
    gnrt_from_to = gnrt_from + gnrt_to


    # From-To
    (x, y) = (48, 111)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_from_to, fill=color, font=tpwr)
    (x, y) = (428, 117)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_from_to, fill=color, font=tpwrsml)

    # Date
    (x, y) = (55, 193)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_date, fill=color, font=tpwrmed)
    (x, y) = (428, 165)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), gnrt_date, fill=color, font=tpwrsml)

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

    # save the edited image
    image.save("Ticket_"+gnrt_pnr+'.png')
    image.show()


menu()

exit()