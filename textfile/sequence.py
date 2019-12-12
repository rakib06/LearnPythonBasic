# Python code to convert string to list
def Convert(string):
    li = list(string.split("-"))
    return li


# Open a file
fo = open("test.txt", "r+")
print("Name of the file: ", fo.name)


# function for read all the output line by line and store it to line_list
line = fo.readlines()
line_list = []
for i in range(0, len(line), 5):
    line_list.append(line[i:i+5])


# a dictionary that store the sequence and corresponding cost
my_dict = {'sequence': [], 'cost': []}

# function for make the total cost into integer and remove whitespace
dept = 6
time = 5

# unique_dict key = sequence , item = cost
unique_dict = {}

for i in range(len(line_list)):
    line_list[i][4] = line_list[i][4].replace('\n', '')
    line_list[i][4] = int(line_list[i][4])
    line_list[i][2] = line_list[i][2].replace('\n', '')
    line_list[i][2] = line_list[i][2].replace(' ', '')
    line_list[i][2] = list(line_list[i][2])
    big_list = []
    for char in line_list[i][2]:
        if char.isnumeric():
            # print(char,end=' ')
            big_list.append(int(char))

    # print(big_list)
    # using list comprehension divide it to D*T format
    original_format_sequence = [big_list[i * dept:(i + 1) * dept] for i in range((len(big_list) + dept - 1) // dept)]
    print(original_format_sequence)
    my_dict['sequence'].append(original_format_sequence)
    my_dict['cost'].append(line_list[i][4])
    unique_dict[line_list[i][4]] = original_format_sequence # cost
    print(type(original_format_sequence))
    print(type(line_list[i][4]))


print(my_dict)
print(unique_dict)

# dictionary sorting

x = sorted(unique_dict, key=unique_dict.__getitem__)
print(x)
for i in x:
    print(unique_dict[i])

# to know key and values
print('to know key and values')
for key,value in unique_dict.items():
    print(key, value)

# to know only values:
for item in unique_dict.values():
    print(item)

print(unique_dict.values())
print(list(unique_dict.values()))






