import random


class Sequence:

    def key_sorted_dict(unique_dict):
        dict = {}
        x = sorted(unique_dict, key=unique_dict.__getitem__)

        for i in x:
            dict[i] = unique_dict[i]
        return dict


    def sequence_from_dict(dict):
        sorted_dict = Sequence.key_sorted_dict(dict)
        sequence = []
        for seq in sorted_dict.values():
            sequence.append(seq)
        return sequence


    def sequence_generator_smart(self, dept, period, file_name):
        format_sequence = []
        number_inside = file_name[4:5]
        sequence_file_name = 'sequence_'+str(number_inside)
        path = '../data/sequence_input/dlp '+str(dept)+'-'+str(period)+'/'
        path_new = '../data/sequence_input/dlp 6-5/'
        print(path)

        fo = open(path_new + sequence_file_name + ".txt", "r+")
        line = fo.readlines()
        print('line {}'.format(line))
        line_list = []
        for i in range(0, len(line)//5, ):
            line_list.append(line[i:i + 5])
        print('line_list[0][4] {} Len {} : '.format(line_list[0][4], len(line_list)))
        unique_dict = {}
        for i in range(len(line_list)):
            # for cost
            print('line_list {} and len: {}'.format(line_list, len(line_list)))
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



        dict = Sequence.key_sorted_dict(unique_dict)


        return format_sequence



    def sequence_generator(self,period, department):
        numbers = []

        for j in range(0,period):
            num = []
            for i in range(1,department + 1):
                num.append(i)
            random.shuffle(num)
            numbers.append(num)

        return numbers