"""
        HACKERRANK NESTED LIST
    URL: https://www.hackerrank.com/challenges/nested-list/problem

    TASK: Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

    Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

    Input Format:
                The first line contains an integer, N, the number of students.
                The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.
    
    Sample Input:
                    5
                    Harry
                    37.21
                    Berry
                    37.21
                    Tina
                    37.2
                    Akriti
                    41
                    Harsh
                    39
    Sample Output:
                    Berry
                    Harry
"""
mainList, subList, secondLowestGradeArray, scoreArray = [], [], [], []
for _ in range(int(input())):
    name, score = input(), float(input())
    subList.append(name)
    subList.append(score)
    scoreArray.append(score)
    mainList.append(subList)
    subList = []

scoreArray = list(set(scoreArray))
scoreArray.sort()

for mainItem in range(len(mainList)):
    if(mainList[mainItem][1] == scoreArray[1]):
        secondLowestGradeArray.append(mainList[mainItem][0])

secondLowestGradeArray.sort()
for secondLowestGradeStudentName in secondLowestGradeArray:
    print(secondLowestGradeStudentName)
