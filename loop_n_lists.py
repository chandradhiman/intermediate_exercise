#list === a container of things that are organized in oder from first to last
#hairs = ['brown', 'blond', 'red']
#eyese = ['brown', 'blue', 'green']
#weight = [1,2,3,4]


the_count = [1,2,3,4,5,6]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 'quartes']

#this first kind for-loop goes through a list
for number in the_count:
    print(f"a this is count {number}")

#same as fruits
for fruit in fruits:
    print(f"a fruit of type: {fruit}")

#same as changes
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts

for i in range (0,6):
    print(f"adding {i} to the list")
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too

for i in elements:
    print(f"element was: {i}")










