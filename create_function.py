def do_domthing():
    pass #tell python this function is empty right now

def do_somthing1():
    print("I do somthing")

#now we can call it by its name
do_somthing1()


# now we pass the argument(parameters) with function

def do_somthing2(a, b):
    print("A is Chandra is", a, "python learner", b)

do_somthing2("hello", 1)

def do_somthing3(args):
    a1, b1 = args
    print(f"a1: {a1}, b1: {b1}")
    

    #def === define