# i =0
# numbers =[]

# while i < 8:
#     print(f"At the top is {i}")
#     numbers.append(i)

#     i = i+1 
#     print("Number now: ", numbers)
#     print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#     print(num)

i = 0 
def change_function():
     global i # declare i is global within the function.
     i = 0
     #while i <= 7: # Change condition to <= to include 7
     while i < 7: #change condition to print until its 7.
         print(i, end = " , ") # print i followed by comma
         i = i+1
# #eturn

change_function()
print(i)

# def change_function():
#     for i in range (1,9):
#         print(i, end =" . ")

# change_function()
