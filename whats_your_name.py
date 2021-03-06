"""
        HACKERRANK PYTHON WHATS YOUR NAME CHALLENGE
    
    URL: https://www.hackerrank.com/challenges/whats-your-name/problem

    TASK: You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following: Hello firstname lastname! You just delved into python.

    SAMPLE INPUT:
                    Ross
                    Taylor
    SAMPLE OUTPUT:
                    Hello Ross Taylor! You just delved into python.
"""

def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a, b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
