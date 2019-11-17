
def finding_the_percentage():
    if __name__ == '__main__':
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores

        query_name = input()
        print('{0:.2f}'.format(sum(student_marks[query_name])/len(student_marks[query_name])))


def what_is_your_name():
    def print_full_name(a, b):
        print("Hello " + a + " " + b + "! You just delved into python.")

    if __name__ == '__main__':
        first_name = input()
        last_name = input()
        print_full_name(first_name, last_name)


def list_operation():

    if __name__ == '__main__':
        my_list = []
        cmd_list = []
        N = int(input())
        for j in range(N):
            cmd = input()
            cmd_list.append(cmd)

        for cmd in cmd_list:

            if cmd == 'print':
                print(my_list)

            elif cmd == 'sort':
                my_list.sort()

            elif cmd == 'reverse':
                my_list.reverse()

            elif cmd == 'pop':
                my_list.pop()

            elif cmd.split(' ')[0] =='insert':
                my_list.insert(int(cmd.split(' ')[1]), int(cmd.split(' ')[2]))
            elif cmd.split(' ')[0] == 'remove':
                my_list.remove(int(cmd.split(' ')[1]))
            elif cmd.split(' ')[0] == 'append':
                my_list.append(int(cmd.split(' ')[1]))


# list_operation()
# finding_the_percentage()

def tuples_1():
    if __name__ == '__main__':
        n = int(input())
        integer_list = map(int, input().split())
        t = tuple(integer_list)
        print(hash(t))


# tuples_1()

def swap_string():
    def swap_case(st):
        s = []
        for char in st:
            if char.islower():
                char = char.upper()
                s.append(char)
            elif char.isupper():
                char = char.lower()
                s.append(char)
            else:
                s.append(char)
        st = ''
        for ch in s:
            st += str(ch)
        return st

    if __name__ == '__main__':
        s = input()
        result = swap_case(s)
        print(result)


swap_string()