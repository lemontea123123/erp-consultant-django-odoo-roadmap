"""
Docstring for exercise_2.2
   - Sum of even numbers from 1 to 200 using a loop.  
"""

start_num = 1
end_num = 200
list_of_number = list(range(start_num,end_num + 1))

list_of_even = []
sum = 0

for num in list_of_number:
    if num % 2 == 0:
        list_of_even.append(num)

for num in list_of_even :
    sum += num

print(sum )


