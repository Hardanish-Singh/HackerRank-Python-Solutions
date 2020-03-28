"""
        HACKERRANK PYTHON LISTS CHALLENGE
    URL: https://www.hackerrank.com/challenges/python-lists/problem

    TASK: Consider a list (list = []). You can perform the following commands:
            1) insert index element: Insert integer element at position index.
            2) print: Print the list.
            3) remove element: Delete the first occurrence of integer element.
            4) append element: Insert integer element at the end of the list.
            5) sort: Sort the list.
            6) pop: Pop the last element from the list.
            7) reverse: Reverse the list.
    
    SAMPLE INPUT 0:
                    12
                    insert 0 5
                    insert 1 10
                    insert 0 6
                    print
                    remove 6
                    append 9
                    append 1
                    sort
                    print
                    pop
                    reverse
                    print
    SAMPLE OUTPUT 0:
                    [6, 5, 10]
                    [1, 5, 9, 10]
                    [9, 5, 1]
"""
N = int(input())
lists, temp = [], []

for _ in range(N):
    name, *line = input().split()

    temp = list(map(float, line))
    if(name == 'insert'):
        lists.insert(int(temp[0]), int(temp[1]))

    elif(name == 'print'):
        print(lists)

    elif(name == 'remove'):
        lists.remove(int(temp[0]))

    elif(name == 'append'):
        lists.append(int(temp[0]))

    elif(name == 'sort'):
        lists.sort()

    elif(name == 'pop'):
        lists.pop()

    elif(name == 'reverse'):
        lists.reverse()

    temp = []
