import textwrap

def wrap(string, max_width):
    op = ''
    for i in range(0, len(string), max_width):
        try:
            op += (string[i:i+max_width])+'\n'
        except:
            op += (string[i:])
    return op

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)