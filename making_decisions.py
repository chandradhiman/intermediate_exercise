## in this script your answer based on user decision.


print("""You enter a dark room with two doors.
      Do you go through door #1 or door #2""")

door = input (">")
if door == "1":
    print("There's a gaint  bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")

    if bear =="1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
    print("Bear runs away.")

elif door == 2:
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Bluebarries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understaing revolers yelling melodies")

    insantiny = input(">")

    if insantiny =="1":
        print("Your body survies powered by a mind of jello")
    elif insantiny =="2":
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("You stumble around and fall on knife and die. Good")

('''
from dis import dis

if door =="1":
    print("1")
    bear = input (">")
if bear == "1":
    print("bear 1"):
elif bear =="2":
    print("bear 2")
else:
    print("bear3")

''')