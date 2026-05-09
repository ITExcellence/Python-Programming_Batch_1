# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# n = int(input("enter a num: "))
# count = 0

# while count <= 12:
#     # 9 x 1 = 9
#     print(f"{n} x {count} = {n*count}")
#     count = count + 1
 

import random

num = []
for i in range(100000):
    answer = random.randint(1, 10)
    num.append(answer)
    
    
print(num)
# tries = 10

# print("Guess a number between 1-100: ")

# while tries > 0:
#     print(f"You have {tries} tries left.")
#     tries -= 1
        
#     num = int(input("Enter a num: "))
    
#     if num == answer:
#         print("You found the answer!!")
#         break
    
#     if tries == 0:
#         print(f"You are out of tries. The answer was {answer}")
#         break
    
#     if num > answer:
#         print("Guess is too large. Please try again")
#     else:
#        print("Guess is too small. Please try again") 
        
        
    