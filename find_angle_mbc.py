"""
        HACKERRANK PYTHON Find Angle MBC
    URL: https://www.hackerrank.com/challenges/find-angle/problem    
"""
import math
if __name__ == '__main__':
    side_a, side_b = int(input()), int(input())
    degree_sign = u'\N{DEGREE SIGN}'
    print("%s%s" % (round(math.degrees(math.atan(side_a/side_b))), degree_sign))
