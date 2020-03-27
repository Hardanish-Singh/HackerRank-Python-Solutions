"""
        PYTHON CHECK LEAP YEAR CHALLENGE
    URL: https://www.hackerrank.com/challenges/write-a-function/problem

    Task: We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
          In the Gregorian calendar three criteria must be taken into account to identify leap years:
                                                                                                        1) If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
                                                                                                        2) If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
                                                                                                        3) If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
                                                                                                        4) The year is a leap year (it has 366 days).
                                                                                                        5) The year is not a leap year (it has 365 days).
          
          This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

          Task: You are given the year, and you have to write a function to check if the year is leap or not. Note that you have to complete the function and remaining code is given as template.
    
    Sample Input 0: 
                    1990
    Output:
                    False
"""


def is_leap(year):
    leap = False

    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
