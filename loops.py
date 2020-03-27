"""
        HACKERRANK PYTHON LOOPS CHALLENGE
    URL: https://www.hackerrank.com/challenges/python-loops/problem

    TASK: Read an integer. For all non-negative integers i<N, print i*i, where 1<=N<=20

    Sample Input: 
                    5
    Sample Output:
                    0
                    1
                    4
                    9
                    16 
"""
number = int(input().strip())

for i in range(0, number):
    print(i*i)
