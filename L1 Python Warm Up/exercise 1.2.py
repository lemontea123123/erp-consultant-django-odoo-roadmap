"""
Docstring for exercise 1.2
Shopping total with discount and tax (subtotal → discount → tax → final total).  
"""

from bootstrap import display_menu
from bootstrap import input_nomor

# ask user for how many items
jumlah_barang = input_nomor(dialog="Input jumlah barang (1-100):",choices=list(range(1,101)))
print()

subtotal = 0
discount_percent = 20
tax_percent = 10

for i in range(jumlah_barang):
    number = i + 1
    print("Harga barang ke-",number,":")
    valid = False
    harga_barang = None

    while(not valid):
        try:
            harga_barang = int(input())
            valid = True
            subtotal = subtotal + harga_barang
        except ValueError:
            print("test")

discount_amount = subtotal * (discount_percent/100)
taxable_amount = subtotal - discount_amount
tax_amount = taxable_amount * (tax_percent/100)
final_total = taxable_amount + tax_amount

print("Subtotal : Rp.",subtotal)
print("Discount (",discount_percent,"%): Rp.",discount_amount)
print("Tax Amount (",tax_percent,"%): Rp.",tax_amount)
print("Final Total : Rp.",final_total)
    




