def alternative_symbol():
    height = int(input("Enter the height of the pyramid: "))

    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")
    
        for j in range(2*i + 1):
            if j % 2 == 0:
                print("*", end="")
            else:
                print("$", end="")
    
        print()
        
def name():
    name = str(input("Input your name: "))
    
    for i in range(len(name)):
        spaces = " " * (len(name) - i - 1)
        letters = " ".join([name[j] for j in range(i+1)])
        print(spaces + letters)

alternative_symbol()
name()
