"""
   - Temperature converter C ↔ F (input a number, output converted value).  
"""
from bootstrap import display_menu

user_choice = display_menu(pilihan_menu=["F","C"])
print("Input A Number:")
user_input = float(input())
input_result = None
string_result = None

if(user_choice == 1):
    input_result = (user_input*9) / 5 + 32
    string_result = str(input_result) + " Fahrenheit"
elif(user_choice == 2):
    input_result = (user_input - 32) * 5 / 9
    string_result = str(input_result) + " Celcius"

print("Result is ",string_result)






