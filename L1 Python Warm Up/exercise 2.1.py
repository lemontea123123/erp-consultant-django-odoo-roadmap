"""
Docstring for exercise 2.1
   - Age classifier: ask age, print child/teen/adult/senior.  

"""

from bootstrap import *

input_umur = input_nomor(dialog="Input Umur (1-100)",choices = list(range(1,101)))

child_flag = input_umur >= 0 and input_umur < 13
teen_flag = input_umur >= 13 and input_umur < 20
adult_flag = input_umur >= 20 and input_umur < 60
senior_flag = input_umur >= 60

if(child_flag):
    print("You are a child")
elif(teen_flag):
    print("You are a teen")
elif(adult_flag):
    print("You are an adult")
elif(senior_flag):
    print("You are a senior")



