# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

my_age = round(90 - int(age))

Days = round(my_age*365)
Weeks = round(my_age*52)
Months = round(my_age*12)

print(f"You have {Days} days, {Weeks} weeks, and {Months} months left.")