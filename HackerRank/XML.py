# Link of this problem:
# https://www.hackerrank.com/contests/python-tutorial/challenges/xml-1-find-the-score/leaderboard

import sys
import xml.etree.ElementTree as etree
def get_attr_number(root):
    # n = int(input())
    xml = ''''''
    count = 0
    for i in range(n):
        x = str(input())
        if x.__contains__('=') :
            c = x.count('=')
            count += c
    return count


if __name__ == '__main__':
    # sys.stdin.readline()
    # xml = sys.stdin.read()
    xml = '''
    <feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>'''
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(root)
    print(len(root))
    for item in root:
        print(item, end=' ')
    # print(get_attr_number(root))
''' xml = <feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>'''