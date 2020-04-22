"""
        HACKERRANK PYTHON FIND A STRING CHALLENGE
    URL: https://www.hackerrank.com/challenges/find-a-string/problem

    TASK: In this challenge, the user enters a string and a substring. 
    You have to print the number of times that the substring occurs in the given string. 
    String traversal will take place from left to right, not from right to left.

    SAMPLE INPUT:
                  ABCDCDC
                  CDC
    SAMPLE OUTPUT:
                  2  
"""


def count_substring(string, sub_string):
    c = 0
    for i in range(len(string)):
        if((len(string) - i) >= len(sub_string)):
            flag = False
            for j in range(len(sub_string)):
                if(string[i] == sub_string[j]):
                    i = i + 1
                else:
                    flag = True
                    break
            if(flag == False):
                c = c + 1
        else:
            break
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
