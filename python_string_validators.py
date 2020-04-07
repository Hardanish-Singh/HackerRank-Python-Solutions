"""
        PYTHON HACKERANK STRING VALIDATORS
    URL: https://www.hackerrank.com/challenges/string-validators/problem

    TASK: Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
          You are given a string S. Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

    SAMPLE INPUT:
                    qA2
    SAMPLE OUTPUT:
                    True
                    True
                    True
                    True
                    True
"""
if __name__ == '__main__':
    s = input()
    flag = False
    for i in range(len(s)):
        if(s[i].isalnum()):
            print(True)
            flag = True
            break
    if(flag == False):
        print(False)
    flag = False
    for i in range(len(s)):
        if(s[i].isalpha()):
            print(True)
            flag = True
            break
    if(flag == False):
        print(False)
    flag = False
    for i in range(len(s)):
        if(s[i].isdigit()):
            print(True)
            flag = True
            break
    if(flag == False):
        print(False)
    flag = False
    for i in range(len(s)):
        if(s[i].islower()):
            print(True)
            flag = True
            break
    if(flag == False):
        print(False)
    flag = False
    for i in range(len(s)):
        if(s[i].isupper()):
            print(True)
            flag = True
            break
    if(flag == False):
        print(False)
    flag = False
