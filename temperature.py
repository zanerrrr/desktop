print("Let's check your temperatur!")
temperature = float(input("What is your temperature?"))
if temperature < 35:
    print("Call your doctor!")
elif temperature == 35 or temperature <= 37 :
    print("You are Ok!")
else:
    print("Possible fever!")