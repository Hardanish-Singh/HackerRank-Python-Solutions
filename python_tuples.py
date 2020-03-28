"""
        HACKERRANK PYTHON TUPLES CHALLENGE
    URL: https://www.hackerrank.com/challenges/python-tuples/problem

    TASK: Given an integer, n and n, space-separated integers as input, create a tuple, t, of those n spaced integers. Then compute and print the result of hash(t)
"""
N = int(input())
line = input().split()
print(hash(tuple(list(map(float, line)))))
