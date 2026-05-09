#  Lists

my_list = [1, 2, 3, 4, 5, 2]
s = "Python"

#  len() -> returns length of the list

# append()
my_list.append(6)

#  insert(postion, value)
my_list.insert(2, 10)

# remove() -> removes first occurance

my_list.remove(2)

# pop()

last_item = my_list.pop()
# print(last_item)
# print(my_list)

# for loop

# for x in range(5,10):
#     print(x)

num_list = [2, 4, 5, 7, 8, 10, 50, 40, 65, 71]
size = len(num_list)
print(size)
even_list = []
odd_list = []

for i in range(size):
    if num_list[i]%2 == 0:
        even_list.append(num_list[i])
    else:
        odd_list.append(num_list[i])
        
print(even_list)
print(odd_list)



# for x in range(0, 10):
#     print(x)