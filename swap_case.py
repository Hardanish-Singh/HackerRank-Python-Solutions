"""
        HACKERRANK SWAP CASE CHALLENGE
    URL: https://www.hackerrank.com/challenges/swap-case/problem

    TASK: You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

    SAMPLE INPUT: 
                    Www.HackerRank.com

    SAMPLE OUTPUT:
                    wWW.hACKERrANK.COM
"""


def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
