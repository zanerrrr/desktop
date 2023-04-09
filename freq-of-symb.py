#counting the letters
# get_char_count = """Write a function: get_char_count(text) that receives
#                a string and outputs a dictionary with the number of single letter applications."""
# letter_dict = {}
# for i in get_char_count:
#     if i in letter_dict:
#         letter_dict[i] += 1
#     else:
#         letter_dict[i] = 1
# print(letter_dict)


#replacing the good and bad values 
def replace_dict_value(d, bad_val, good_val):
   
    new_dict = {}
    for key, value in d.items():
        if value == bad_val:
            new_dict[key] = good_val
        else:
            new_dict[key] = value
    return new_dict

d = {'a': 4, 'b': 56, 'c': 0}
bad_val = 4
good_val = 10
new_dict = replace_dict_value(d, bad_val, good_val)
print(new_dict)

#cleaning dictionary
def clean_dict_value(d, bad_val):
    clean_dict = {}
    for key, value in d.items():
        if value != bad_val:
            clean_dict[key] = value
    return clean_dict


clean_dict = clean_dict_value(d, bad_val)
print(clean_dict)