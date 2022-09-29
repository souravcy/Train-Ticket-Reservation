import smtplib
import random
# create smtp session
s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
# start TLS for E-mail security
s.starttls()
# Log in to your gmail account
s.login("no.reply.ticketreservationportal@gmail.com", "ticketreservationportal")
otp = random.randint(1000, 9999)
otp = str(otp)
# email = no.reply.ticketreservationportal@gmail.com
# password = ticketreservationportal

s.sendmail("no.reply.ticketreservationportal@gmail.com", "mdsaoodkhan007@gmail.com", otp)
print("OTP sent successfully..")
# close smtp session
s.quit()