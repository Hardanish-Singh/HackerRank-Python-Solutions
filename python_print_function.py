"""
        HACKERRANK PRINT PYTHON CHALLENEGE
    URL: https://www.hackerrank.com/challenges/python-print/problem

    Task: Read an integer N, Without using any string methods, try to print the following: 123...N, Note that "..." represents the values in between. 

    Sameple Input:
                    3
    Same Output:
                    123
"""
number = int(input().strip())

for i in range(1, number+1):
    print(i, end="")  # end="", will print results/data in the same line
