#  A. Winter Sale

# x = float(input("X: "))
# p = float(input("P: "))

# u = 1-(x/100)
# ans = p/u

# print(f"{ans:.2f}")


# a = int(input("a: "))
# b = int(input("b: "))

# if abs(a-b) == 1 or abs(a-b) == 0:
#     print("YES")
# else:
#     print("NO") 

# char = input("")

# if char == 'z':
#     print('a')
# elif char == 'Z':
#     print('A')
# else:
#     a = ord(char)+1
#     ans = chr(a)

#     print(ans)


# test_cases = int(input("Test cases: "))
# #  4
# for i in range(test_cases):
#     l = int(input("l: "))
#     r = int(input("r: "))
    
#     sum_odd = 0
#     for j in range(l, r):
#         if j%2 == 1:
#             sum_odd += j
#         print(sum_odd)


# n = int(input("n: "))

# li = list(map(int, input("Enter numbers: ").split()))

# # print(li)

# moves = 0

# for i in range(n-1):
    
#     if li[i+1] < li[i]:
#         diff = li[i] - li[i+1]
#         moves += diff

# print(moves)