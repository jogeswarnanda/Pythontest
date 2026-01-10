import datetime as dt
import smtplib
import random
import pandas 

MY_EMAIL    = "jogeswarnanda2022@gmail.com"
MY_PASSWORD =  "bhmo flxb jngo kuhj"

now = dt.datetime.now()
day_today  = now.day
#print(day_today)
today_tuple = (now.month, now.day)
birthday_data = pandas.read_csv("birthdays.csv")
#print(birthday_data)

birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in birthday_data.iterrows()}
print(f"dict:\n {birthday_dict}")

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    print("Today is birthday!")
    letter = random.randint(1,3)
    with open(f"letter_templates/letter{letter}.txt", "r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])
        print(letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday !!\n\n {letter}".encode("utf-8"))
else:
    print("Today is not birthday!")