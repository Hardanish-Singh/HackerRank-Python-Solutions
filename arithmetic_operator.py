"""
        HACKERRANK ARITHMETIC OPERATOR CHALLENGE
    URL: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

    Task: Read two integers from STDIN and print three lines where:
            1) The first line contains the sum of the two numbers.
            2) The second line contains the difference of the two numbers (first - second).
            3) The third line contains the product of the two numbers.
    
    Input Format: The first line contains the first integer, a. The second line contains the second integer, b. 
    
    Sample Input: 
                    3
                    2
    Sample Output:
                    5
                    1
                    6
"""
number1 = int(input().strip())
number2 = int(input().strip())

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
