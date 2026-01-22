"""
Docstring for exercise_2.3
   - Simple ATM simulator: start with balance, allow withdrawals until user exits or not enough balance.
"""

from bootstrap import *

program_loop = True
balance = 1000000

menu_choice_1 = ["Withdrawal","Exit"]

while(program_loop):
    print("Your Balance is ", balance)
    user_choice_1 = display_menu(pilihan_menu=menu_choice_1)
    if(user_choice_1 == 1):
        jumlah_withdraw = input_nomor(dialog="Input Amount To Withdraw")

        if(jumlah_withdraw <= balance):
            balance = balance - jumlah_withdraw
            print("Balance deducted ! Successfully Withdrawn $",jumlah_withdraw)
            user_loading()
        else:
            print("Balance Not Enough ! Exiting Program")
            user_loading()
            program_loop = False

    elif(user_choice_1 == 2):
        print("\nExiting Program")
        user_loading()
        program_loop = False

    print()