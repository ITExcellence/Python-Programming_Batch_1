"""
Strong password:
 - length greater 8 characters
 - must contain at least 1 number
 - must contain at least 1 special character
 - must not match with any banned password
 
Take input until a password is strong

special_char = '!@#$%^&*()'

if passw[i] in '0123456789':

banned-password = ['password*123', '@bcd1234']

"""

special_char = '!@#$%^&*()'
nums = '0123456789'

while True:
    password = input('Enter your password: ')
    is_long = False
    is_num = False
    is_special = False
    
    if len(password) >= 8:
        is_long = True
    
    for char in password:
        if char in special_char:
           is_special = True
           
        if char in nums:
            is_num = True
    
     
    if is_long and is_num and is_special:
        print("Strong password. Good Job!")
        break
    else:
        if is_long == False:
            print("Too short, password must be at least 8 characters.")
        if is_num == False:
            print("Must contain at least one digit")
        if is_special == False:
            print("Must contain at least one special character `!@#$%^&*()`")
        print("Weak password. Try again.")
