### Part Four -- your code goes here. 
import random
list =[]

for i in range(10):
    i = random.randint(1,101)
    
    list.append(i)

print("Old list:",list)

pointer = 0
while pointer < len(list):
    if list[pointer] % 2 == 0: 
        list.pop(pointer)       
    else:
        pointer += 1 
print("New list:", list) 

