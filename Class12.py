#  Sort Numbers

# num_list = [1, 5, 6, 2, 4, 3]
# size = len(num_list)


# for i in range(size):
#     for j in range(size):
#         # print(f"i = {i} | j = {j}")
#         if num_list[i] > num_list[j]:
#             temp = num_list[i]
#             num_list[i] = num_list[j]
#             num_list[j] = temp
#     print(num_list)



# Loops

# n = int(input(""))

# for i in range(1, n+1):
#     print(i)


odd = 0
even = 0
positive = 0
negative = 0 
n = 5

if n%2 == 0:
    even = even + 1
else:
    odd = odd + 1
    
num = 5

for i in range(num):
    a = int(input())
    
    