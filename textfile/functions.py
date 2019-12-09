# input file name
# return a dictionary with cost and sequence
import operator
def key_sorted_dict(unique_dict):
    dict = {}
    x = sorted(unique_dict, key=unique_dict.__getitem__)

    for i in x:
        dict[i] = unique_dict[i]
    return dict


def sequence_from_dict(dict):
    sorted_dict = key_sorted_dict(dict)
    sequence = []
    for seq in sorted_dict.values():
        sequence.append(seq)
    return sequence


def sequence_and_cost_convert_from_txt(path, file_name, dept):
    # Open the file
    fo = open(path+file_name+".txt", "r+")
    # print("Name of the file: ", fo.name)
    # fo = open("../textfile/output/test.7.txt","r+")

    # function for read all the output line by line and store it to line_list
    line = fo.readlines()
    line_list = []
    for i in range(0, len(line), 5):
        line_list.append(line[i:i + 5])
    unique_dict = {}
    for i in range(len(line_list)):
        line_list[i][4] = line_list[i][4].replace('\n', '')
        cost = line_list[i][4] = int(line_list[i][4])

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
        format_sequence = [big_list[i * dept:(i + 1) * dept] for i in
                                    range((len(big_list) + dept - 1) // dept)]
        unique_dict[cost] = format_sequence
    dict = key_sorted_dict(unique_dict)
    sequence = sequence_from_dict(dict)
    return dict,sequence


path = "../textfile/output/test"
file_name = '.7'
dict, sequence = sequence_and_cost_convert_from_txt(path,file_name,6)

# best way for dictionary sorting but returns list
sorted_word = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_word)
x = type(sorted_word)
print(str(x))
for cost, sequence in sorted_word:
    print(sequence, '  Cost: ', cost)