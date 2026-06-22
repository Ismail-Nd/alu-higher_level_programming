## This program calcualtes user inputs and returns complete time in days, hours, minutes, seconds.

## We will start by asking the user to enter the number of seconds.

data = int(input("Enter the number of seconds: "))

## We will then calculate the number of days, hours, minutes, seconds.

days = data // 86400
total = data % 86400
hours = data // 3600 
data = data % 3600
minutes = data // 60
data = data % 60
seconds = data

print(f"The time is {hours} hour(s), {minutes} minute(s), {seconds} second(s).")

