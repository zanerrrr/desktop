for i in range(len(name)):
        spaces = " " * (len(name) - i - 1)
        letters = " ".join([name[j] for j in range(i+1)])
        print(spaces + letters)