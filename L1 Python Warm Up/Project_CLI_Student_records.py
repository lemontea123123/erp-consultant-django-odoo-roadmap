"""
Docstring for Project_CLI_Student_records
4. **Mini project – CLI Student Records**  
   - Menu‑based app in terminal:  
     - Add student (name, age, scores list).  
     - List all students.  
     - Show top student by average score (highest average wins). 
"""

from bootstrap import *


#Main Variables
students_list = []
score_list_length = 3 
menu_choices_1 = ["Add Student","List All Students","Ranking From Highest Average","Exit"]
program_loop = True


#Supporting Functions

students_a = [
    {"name": "Aaron"},
    {"name": "Charlie"},
    {"name": "Evelyn"},
    {"name": "Liam"},
    {"name": "Zara"},
]

students_b = [
    {"name": "Bella"},
    {"name": "Daniel"},
    {"name": "Frank"},
    {"name": "Nora"},
    {"name": "Oscar"},
]



#Sort function
def merge(arr1,arr2,score_based=False):
    #Global Variable students_list

    arr1_len = len(arr1)
    arr2_len = len(arr2)
    total_length = arr1_len + arr2_len
    i1 = 0
    i2 = 0
    choose_i1 = False
    chosen_ele = None


    new_arr = []

    #Core of merge sort algo
    for i in range(total_length):
        
        i1_oob = i1 >= arr1_len
        i2_oob = i2 >= arr2_len

        i1_ele = None
        i2_ele = None

        either_oob = i1_oob or i2_oob
        none_oob = not either_oob

        if(not i1_oob):
            i1_ele = arr1[i1]
        else:
            choose_i1 = False

        if(not i2_oob):
            i2_ele = arr2[i2]
        else:
            choose_i1 = True
        
        if(none_oob):
            i1_name = i1_ele["name"].lower()
            i2_name = i2_ele["name"].lower()
            #Comparison is a variable that determins if i1 should be in front of i2
            if(not score_based):
                comparison = i1_name < i2_name

            if(score_based):
                i1_score = i1_ele["average"]
                i2_score = i2_ele["average"]
                score_comparison = i1_score - i2_score
                if(score_comparison == 0):
                    #If score comparison is neutral then order by name
                    comparison = i1_name < i2_name
                elif(score_comparison > 0):
                    comparison = True
                elif(score_comparison < 0):
                    comparison = False
            
            choose_i1 = comparison
        
        if(choose_i1):
            chosen_ele = arr1[i1]
            i1 += 1
        else:
            chosen_ele = arr2[i2]
            i2 += 1

        new_arr.append(chosen_ele)
    
    return new_arr


def merge_sort(arr,score_based = False):
    #Implement iterative merge sort
    arr_length = len(arr)
    sub_arr_length = 1
    sub_arr_left = None
    sub_arr_right = None

    left_start_i = 0

    new_arr = arr[:]
    temp_arr = []

    while(sub_arr_length <= arr_length):
        while(left_start_i <= arr_length):
            left_end_i = left_start_i + sub_arr_length
            right_start_i = left_end_i
            right_end_i = right_start_i + sub_arr_length

            sub_arr_left = new_arr[left_start_i:left_end_i]
            sub_arr_right = new_arr[right_start_i:right_end_i]

            merged_arr = merge(sub_arr_left,sub_arr_right,score_based)

            temp_arr.extend(merged_arr)
            left_start_i = right_end_i

        left_start_i = 0
        new_arr = temp_arr
        temp_arr = []
        sub_arr_length = sub_arr_length * 2

    return new_arr






#Functions
def search_student(student_name):
    #Global Variable students_dict

    found_flag = False

    for student in students_list:
        if (student['name'] == student_name):
            found_flag = True
            break

    return found_flag


def add_route_1():
    #Global Variable students_dict 

    #Create a student's list
    student_object = {}
    student_name = None
    student_age = None
    student_scores = []
    student_average = 0

    #Input name check if name already exists
    print("Input Valid Student Name")
    student_name = input()

    #Student must not exist before
    student_exists = search_student(student_name)
    
    name_invalid = student_exists

    if(student_exists):
        print("Student name exists !\n")
    
    if(name_invalid):
        user_loading()
        return False

    #input Age (reasonable range)
    student_age = input_nomor(dialog="Input Student's Age: ")

    age_oob = student_age < 0 or student_age >= 30

    age_invalid = age_oob

    if(age_oob):
        print("Please Input Reasonable Student Age !\n")

    if(age_invalid):
        user_loading()
        return False

    #Input array of scores
    
    for i in range(score_list_length):
        input_loop = True
        while(input_loop):
            #Keep on looping this nth for loop if the user input wrong kind of score format
            dialog_arg = "Input "+str(i+1)+"th score:"
            score = input_nomor(dialog=dialog_arg)

            #Checks
            score_oob = score<0 or score>100

            score_invalid = score_oob

            if(score_invalid):
                print("Please input score in the reasonable range!")
                input_loop=True
            else:
                input_loop = False
                student_scores.append(score)

    
    #Calculate average and store together with the student object
    total_score = 0

    for score in student_scores:
        total_score += score

    student_average = total_score / len(student_scores)

    student_object['name'] = student_name
    student_object['age'] = student_age
    student_object['scores'] = student_scores
    student_object['average'] = student_average

    students_list.append(student_object)

def list_all_route_1():
    #Global Variable students_list

    sorted_list = merge_sort(students_list,score_based=False)
    print("Displaying All Students:")
    for index , student in enumerate(sorted_list):
        
        print(index+1,".",student["name"])

def ranking_route_1():
    #Global Variable students_list

    sorted_list = merge_sort(students_list,score_based=True)
    print("Displaying All Students:")
    for index , student in enumerate(sorted_list):
        
        print(index+1,".",student["name"],"=>",student["average"])

students_list = [
    {"name": "Nora",    "average": 78.5},
    {"name": "Aaron",   "average": 92.0},
    {"name": "Zara",    "average": 81.0},
    {"name": "Frank",   "average": 69.5},
    {"name": "Charlie", "average": 88.0},
    {"name": "Bella",   "average": 74.0},
    {"name": "Oscar",   "average": 85.0},
    {"name": "Liam",    "average": 90.0},
    {"name": "Evelyn",  "average": 92.0},  # same as Aaron
    {"name": "Daniel",  "average": 81.0},  # same as Zara
]

while(program_loop):
    user_choice_1 = display_menu(pilihan_menu = menu_choices_1)

    add_route = user_choice_1 == 1
    list_all_route = user_choice_1 == 2
    ranking_route = user_choice_1 == 3
    exit_route = user_choice_1 == 4

    print()

    if(add_route):
        add_route_1()
    elif(list_all_route):
        list_all_route_1()
        user_loading()
    elif(ranking_route):
        ranking_route_1()
        user_loading()
    elif(exit_route):
        print("Exiting Program...")
        program_loop = False
        user_loading()

        