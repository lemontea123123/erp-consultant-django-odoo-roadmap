"""
Docstring for exercise 1.3

   - Split an invoice amount into N installments (print each installment amount).
"""

from bootstrap import *

total_amounts = 505
n_installments = 10

base = int(total_amounts / n_installments)
remainder = total_amounts % n_installments

amounts_list = []

for i in range(n_installments):
    amounts_list.append(base)

for i in range(remainder):
    amounts_list[i] += 1


print("Monthly Installments:")
for i,amount in enumerate(amounts_list):
    order = i + 1

    print("Month -",order," \t-> $",amount)


