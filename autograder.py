labs = int(input('Enter the number of labs completed: '))
quiz = int(input('Enter the number of quizzes completed: '))
assignment_1 = int(input('Enter grade for Assignment 1: '))
assignment_2 = int(input('Enter grade for Assignment 2: '))
assignment_3 = int(input('Enter grade for Assignment 3: '))
assignment_4 = int(input('Enter grade for Assignment 4: '))
assignments_avg = (assignment_1 + assignment_2 + assignment_3 + assignment_4)/4
midterm_1 = int(input('Enter grade for Midterm 1: '))
midterm_2 = int(input('Enter grade for Midterm 2: '))
midterms_avg = (midterm_1 + midterm_2)/2
final = int(input('Enter grade for Final Exam: '))
preps = int(input('Enter grade for Midterms and Final Preparation: '))
if labs >= 6:
    labs_grade = 20
else:
    labs_grade = (labs/6)*20
if quiz >= 6:
    quiz_grade = 15
else:
    quiz_grade = (quiz/6)*15
final_grade = (labs_grade + quiz_grade) + (assignments_avg*0.16) + (midterms_avg*0.25) + (final*0.18) + (preps*0.06)
final_grade = round(final_grade)
print('Your grade is: ', final_grade)
