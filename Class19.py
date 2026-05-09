# Exercise 1

# num = 1

# while num < 11:
#     print(num)
    
#     num += 1


# Exercise 2

# for i in range(-10, 0):
#     print(i)

# Exercise 3

# for i in range(0, 5):
#     print(i)
#     if i == 4:
#         print("Done!")

# Exercise 4

# num = int(input(" Enter a number: "))
# sum_num = 0
# for i in range(1, num+1):
#     print(f"When i is: {i} | Sum is: {sum_num}")
    
#     sum_num += i
    
# print(f" Sum: {sum_num}")


# Exercise 7

"""
Given a list of numbers, iterate through it and print numbers that satisfy these conditions:


-- The number must be divisible by five.
-- If the number is greater than 150, skip it and move to the next.
-- If the number is greater than 500, stop the loop entirely.


"""

nums = [12, 50, 80, 76, 56, 55, 600, 346, 60, 21]
#       0   1    2   3   4   5   6    7   8   9

# # for i in range(len(nums)):
# #     print(i, end=": ")
# #     print(nums[i])

# for num in nums:
    
#     if num > 500:
#         break
#     elif num > 150:
#         continue
#     elif num % 5 == 0:
#         print(num)

size = len(nums)
last_index = size - 1

for i in range(last_index, -1, -1):
    print(nums[i], end=" ")