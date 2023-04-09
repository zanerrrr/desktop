numbers = input("Enter numbers separated by space: ")
print("\n")
user_list = numbers.split()
print("list: ", user_list)
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

avg = round(sum(user_list) / len(user_list), 2)
print("Average of your list: ", avg)

minvalueofnumbers = min(user_list)
print("The smallest value: ", minvalueofnumbers)
print("\n")
maxvalueofnumbers = max(user_list)
print("The biggest value: ", maxvalueofnumbers)
print("last three numbers: ", user_list[-3:])
print("first three numbers: ", user_list[:3])