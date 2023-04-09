print("Do you need a bonus?")

years = int(float(input("How many years have you worked here?")))
salary = int(float(input("what is your salary?")))
bonus = 0

if years >= 2:
    bonus = (salary * 0.15) * years
    print(f"Your bonus is {bonus}! ")
else:
    print("You have not earned a bonus!")

bonus_salary = bonus + salary
print(f"At the end you will receive {bonus_salary}! ")