import smtplib
my_email = "jogeswarnanda2022@gmail.com"
password =  "bhmo flxb jngo kuhj"

try:
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
    to_addrs="jogeswarnanda@zohomail.in", 
    msg="Subject:Hello\n\nThis is the body of my email")
    connection.quit()
    
except Exception as e:
    print(f"Error: {e}")
