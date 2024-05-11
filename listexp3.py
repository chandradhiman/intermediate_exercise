family1 = ['bittu', 'shalu', 'shefali', 'samira']
family2 = ['chandra', 'chanchal', 'aman', 'mom']
friend = ['arpita', 'manu', 'gagan', 'jinen']
change = [1,2,3,4]

def change_function (my_family1, my_family2, my_friend):
    for i, (a,b,c) in enumerate(zip(my_family1, my_family2, my_friend)):
        print(f"This count{i}")
        print(f"This is family1 member: {a}")
        print(f"This is family2 member: {b}")
        print(f"This is Friend member: {c}")
    return

change_function(family1, family2, friend)
