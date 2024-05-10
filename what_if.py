#if statement

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The wolrd is doomed!")

if people>cats:
    print("Not man cats! The wolrd is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5


if people >= dogs:
    print("People are greater or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")


#dis()IT

#from dis import dis

#dis ('''
 #    if people<cats: 
  #   print("Too many cats! The world is doomed!")
   #  ''')