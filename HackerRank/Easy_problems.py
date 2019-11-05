
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


finding_the_percentage()