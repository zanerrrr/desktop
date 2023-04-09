#not sure if this is correct tho
numb = int(input("Input a number from 1 to 100!"))
if numb % 5 == 0 and numb % 7 == 0:
    print("FizzBuzz")
elif numb % 5 == 0:
    print("Fizz")
elif numb % 7 == 0:
    print("Buzz")
else:
    print(numb)

#this have to be correct        
for numb in range(1, 101):
    if numb % 5 == 0 and numb % 7 == 0:
        print("FizzBuzz")
    elif numb % 5 == 0:
        print("Fizz")
    elif numb % 7 == 0:
        print("Buzz")
    else:
        print(numb)