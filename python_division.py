"""
        PYTHON DIVISION
    URL: https://www.hackerrank.com/challenges/python-division/problem

    Task: Read two integers and print two lines. The first line should contain integer division, a//b, 
    The second line should contain float division, a/b

    Sample Input: 
                    4
                    3
    Sample Output:
                    1
                    1.33333333333
"""

number1 = int(input().strip())
number2 = int(input().strip())

print(number1//number2)
print(number1/number2)
