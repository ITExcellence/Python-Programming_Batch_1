
# #  Global 
# x = 10

# def fn():
#     #  Local
#     x = 5
    
#     return x
    

# a = fn()
# print(a)
# print(x)

price = "Not"

if isinstance(price, (int, float)):
    print("Okay!!")
    
if not isinstance(price, (int, float)):
    print("Not int or float")
