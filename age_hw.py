
print("This is a programm to determine in how many years you will be 100!")
user_name = input("What is your name? ")
print(f"Nice to meet you, {user_name} !")
user_age = int(input(f"How old are you, {user_name} ? "))
if (user_age >= 100):
    print("You already are 100 years old!")
elif (user_age <= 0) :
    print(f"{user_name}, try again, when you are born!")
else:
    time_until_100 = 100 - user_age
    print(f"{user_name}, you will be 100 in {time_until_100} years! ")

yes_no = input("Do you want to know what year you will turn 100? (Y/N) ")
if (yes_no == "y"):
    year = int(input("Ok, enter your birth year! "))
    #current_year = date.today()
    turn_100 = year + 100
    print("You will turn 100 in ", turn_100)
else :
    print("Ok, then bye! ")
    