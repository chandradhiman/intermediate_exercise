cricket = ['sachin', 'virat', 'arjun', 'kisan','adi']
actor = ['rajkumar', 'ranveer', 'sahid', 'fardeen', 'runbeer']
changes = ['alia', 2 , 5, 'kiara', 'kajol']


def chandra_function(chand_cricket, chand_actor):
    for i, (b,c) in enumerate (zip(chand_cricket, chand_actor)):
        print(f"This is count{i}")
        print(f"indian cricketer name: {b}")
        print(f"This is actor name: {c}")
    return

chandra_function(cricket, actor)

