"""
        HACKERRANK FIND THE RUNNER UP SCORE
    URL: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

    TASK: Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

    INPUT FORMAT: The first line contains N. The second line contains an array A[] of n integers each separated by a space.

    SAMPLE INPUT 0:
                    5
                    2 3 6 6 5
    OUTPUT:
                    5
"""

n = int(input())
"""
    list(set(map(int, input().split()))) 
        IS BROKEN INTO 3 PARTS
            1)  map(int, input().split())                       (TAKE MULTIPLE INPUTS ON THE SAME LINE)
            2)  set(map(int, input().split()))                  (CONVERT INPUT TO SET, CONVERTING TO SET DATATYPE WILL REMOVE DUPLICATES)
            3)  list(set(map(int, input().split())))            (LAST CONVERT TO LIST)
"""
arr = list(set(map(int, input().split())))
arr.sort()
print(arr[-2])  # PRINTS THE SECOND LARGEST NUMBER
