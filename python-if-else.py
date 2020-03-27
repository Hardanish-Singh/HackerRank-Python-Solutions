"""
        HACKERRANK PYTHON-IF-ELSE CHALLENGE
    
    URL: https://www.hackerrank.com/challenges/py-if-else/problem

    Task: Given an integer, n , perform the following conditional actions:
            1) If n is odd, print Weird
            2) If n is even and in the inclusive range of 2 to 5, print Not Weird
            3) If n is even and in the inclusive range of 6 to 20, print Weird
            4) If n is even and greater than 20, print Not Weird
    
    Input Format: A single line containing a positive integer n, where 1<=n<=100

    Output Format: Print Weird if the number is weird; otherwise, print Not Weird.
    
"""
n = int(input().strip())
if(1 <= n <= 100):
    if(n % 2 == 0):
        if(2 <= n <= 5):
            print("Not Weird")
        elif(6 <= n <= 20):
            print("Weird")
        elif(n > 20):
            print("Not Weird")
    elif(n % 2 != 0):
        print("Weird")
