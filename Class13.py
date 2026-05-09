# # Task 1

# n = int(input("Enter days: "))

# years = n//365
# remain_days = n%365
# months = remain_days//30
# days = remain_days%30

# print(f"Years: {years}\nMonths: {months}\nDays: {days}")


# n = int(input(""))

# for i in range(1, 13):
#     print(f"{n} * {i} = {n*i}")


# a = int(input(""))
# b = int(input(""))

# for i in range(a, b+1):
#     if i%4 == 0 or i%7 == 0:
#         print(i, end=" ")



password = "1999"

while True:
    i = int(input(""))
    if i == password:
        print("Correct")
        break
    else:
        print("Incorrect")