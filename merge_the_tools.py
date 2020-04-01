"""
        HACKERRANK MERGE THE TOOLS CHALLENGE
    URL: https://www.hackerrank.com/challenges/merge-the-tools/problem

    SAMPLE INPUT:
                    AABCAAADA
                    3 
    SAMPLE OUTPUT:
                    AB
                    CA
                    AD
"""


def find_unique_characters_in_a_string(string):
    unique_character_list = []
    for i in range(len(string)):
        flag = False
        for j in range(0, i):
            if(string[i] == string[j]):
                flag = True
                break
        if(flag == True):
            continue
        unique_character_list.append(string[i])
    return unique_character_list


def merge_the_tools(string, k):
    for i in range(0, len(string)):
        if((i+1) % k == 0):
            unique_characters_list = find_unique_characters_in_a_string(
                string[i-(k-1):i+1])
            print(''.join(unique_characters_list))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
