"""
        HACKERRANK PYTHON FINDING THE PERCENTAGE
    URL: https://www.hackerrank.com/challenges/finding-the-percentage/problem

    TASK: You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N  followed by the names and marks for N
          students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
    
    INPUT FORMAT: The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

    OUTPUT FORMAT: Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

    SAMPLE INPUT:
                    3
                    Krishna 67 68 69
                    Arjun 70 98 63
                    Malika 52 56 60
                    Malika
    SAMPLE OUTPUT:
                    56.00
"""
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

avg = 0
for key in student_marks:
    if(key == query_name):
        for i in range(len(student_marks[key])):
            avg = avg + student_marks[key][i]

print("{:0.2f}".format(avg/(i+1)))
