#  Strings    

# txt1 ="Python123Programming"

# print(txt1)
# print(txt1.strip())
# print(txt1.upper())
# print(txt1.lower())
# print(txt1.replace('P', 'u'))
# print(txt1.isalpha())
# print(txt1.isalnum())
# print(txt1.isdigit())


# new_txt = txt1 + txt2
# print(len(new_txt))
# first = txt1[::-1]
# print(first)

# email = "test@email.com"

# if "@" in email:
#     print("Valid email")
# else:
#     print("Invalid email")

#  Palindrome

# word = input("Enter a word: ")
# word = word.lower()
# new_word = word[::-1]

# if word == new_word:
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")

#  Password generator

# name = "abdurrahman"

# password = name.lower().replace('a', '$').replace('r', '5').replace('b', '#')

# final_password = password + str(len(password))

# print(final_password)

#  List

my_list = [10, 10, 20, 30]
a_list = ["Mango", "Apple", "Kiwi"]
b_list = ["Mango", 10, 50, True]

my_list.append(40)
print(my_list)
my_list.insert(1, 50)
print(my_list)
my_list.remove(10)
print(my_list)
my_list.pop()
print(my_list)