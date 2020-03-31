"""
        HACKERRANK PYTHON STRING MUTATIONS
    URL: https://www.hackerrank.com/challenges/python-mutations/problem

    TASK: We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed). Let's try to understand this with an example. You are given an immutable string, and you want to make changes to it.

    SAMPLE INPUT:
                    abracadabra
                    5 k
    SAMPLE OUTPUT:
                    abrackdabra
"""

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
