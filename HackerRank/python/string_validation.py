if __name__ == '__main__':
    s = input()
    print_dict = {1: False, 2: False, 3: False, 4: False, 5: False}

    my_list = [x for x in s]
    for item in my_list:
        if item.isalnum():
            print_dict[1] = item.isalnum()
        if item.isalpha():
            print_dict[2] = item.isalpha()
        if item.isdigit():
            print_dict[3] = item.isdigit()
        if item.islower():
            print_dict[4] = item.islower()
        if item.isupper():
            print_dict[5] = item.isupper()

    for item in print_dict:
        print(print_dict[item])


