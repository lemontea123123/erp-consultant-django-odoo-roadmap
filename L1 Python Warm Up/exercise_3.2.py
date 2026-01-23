"""
Docstring for exercise_3.2
   - Contact book with `dict`: add, search, delete contacts by name.
"""

from bootstrap import *

#supporting functions


def add_menu_1():
   #uses global variables main_dict

   print("Input New Contact Name: ")
   user_input_1 = input()

   not_exist_flag = user_input_1 not in main_dict.keys()

   valid_flag = not_exist_flag

   if(not_exist_flag):
      print("Input Contact Number: ")
      user_input_2 = input()

      main_dict[user_input_1] = user_input_2
      print("Added",user_input_1,"to contacts.\n")
   else:
      print("Contact Name Exists Already!\n")

   user_loading()

   #Wheter executement is true or some error along the way
   if(valid_flag):
      return True
   else:
      return False

def search_menu_1():
   #Global Variable main_dict

   print("Search Name: ")
   user_input_1 = input()

   #Checks
   found_flag = user_input_1 in main_dict.keys()

   valid_flag = found_flag

   if(found_flag):
      print("Contact Found!")
      print(user_input_1 , "->" ,main_dict[user_input_1])
      print()
   else:
      print("Contact Not Found!\n")

   user_loading()

   if(valid_flag):
      return True
   else:
      return False

def delete_menu_1():
   #Global variable main_dict
   print("Delete Name: ")
   user_input_1 = input()

   #Checks
   found_flag = user_input_1 in main_dict.keys()

   valid_flag = found_flag

   if(found_flag):
      print("Deleting Contact!")
      main_dict.pop(user_input_1)
      print()
   else:
      print("Contact Not Found!\n")

   user_loading()

   if(valid_flag):
      return True
   else:
      return False


main_dict = {}

menu_choice_1 = ["Add","Search","Delete","Exit"]

program_loop = True

while(program_loop):
   #Display menu
   pilihan_user_1 = display_menu(pilihan_menu = menu_choice_1)

   add_flag = pilihan_user_1 == 1
   search_flag = pilihan_user_1 == 2
   delete_flag = pilihan_user_1 == 3
   exit_flag = pilihan_user_1 == 4

   if(add_flag):
      add_menu_1()
   elif(search_flag):
      search_menu_1()
   elif(delete_flag):
      delete_menu_1()
   elif(exit_flag):
      print("Exiting Program...\n")
      user_loading()
      program_loop = False

