"""
Docstring for exercise_3.1
   - Grade calculator: list of scores → average → letter grade using a function.  
"""
from bootstrap import *

list_of_scores = [80,95,99,100]
list_length = len(list_of_scores)
total_score = 0
avg_score = 0


for score in list_of_scores:
    total_score = total_score + score

avg_score = total_score / list_length
grade = None

if(avg_score >= 90 ):
    grade = "A"
elif(avg_score >= 80):
    grade = "B"
elif(avg_score >= 70):
    grade = "C"
elif(avg_score >= 60):
    grade = "D"
elif(avg_score <60):
    grade = "F"

print("Your grade is ",grade)
