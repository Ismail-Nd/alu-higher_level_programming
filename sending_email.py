import email
import smtplib
from email.message import EmailMessage

Name = input("What's your name: ")
age = int(input("What is your age: "))

if age >= 18:
    print(f'Hello {Name}, you are allowed to enter because you are above the permitted age.')

    email_address = input(f"Enter your email (e.g. {Name}@gmail.com): ")

    msg = EmailMessage()
    msg['From'] = "ndismail007@gmail.com"
    msg['To'] = email_address

    msg['subject'] = 'Entry Ticket for (f"{Name}")'
    msg.set_content(f"Hello {Name}, your ticket is confirmed 🎟️")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('ndismail007@gmail.com', 'hqep mppv pdqq bwmy')
        smtp.send_message(msg)

    print("Email successfully sent!")

else:
    print("You are not allowed to enter.")
