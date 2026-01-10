import datetime as dt
import smtplib
import random

MY_EMAIL  = "jogeswarnanda2022@gmail.com"
MY_PASSWORD =  "bhmo flxb jngo kuhj"

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 6:
    print("Monday")
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    print(random.choice(quotes))

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="jogeswarnanda@zohomail.in",
        msg=f"Subject:Monday Motivation !!\n\n {random.choice(quotes)}".encode("utf-8"))


# print(now)
# print(type(now))
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)
# print(now.weekday())

# data_of_birth = dt.datetime(year=1990, month=1, day=15, hour=4)

# print(data_of_birth)