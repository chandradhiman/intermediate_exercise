email = {
    "From": "chandradhiman13@gmail.com",
    "To": "chandradhimaneu@gmail.com",
    "Subject": "I have an amazing investment for you !!! "
      };
#function name are variable 

def print_number(x):
    print("Number is", x)

rename_print = print_number
rename_print(100)
print_number(100)

# dictionaries with variables

color = "Red"
corvette = {"color":color}
print("LITTLE", corvette["color"], "CORVETTE")

animal = "Dog"
breed = {"animal":animal}
print("Lucy",breed["animal"], "breed")

#dictionaries with functions

def run():
    print("VROOM")

corvette = {"color":"red", "run":run}
print("My", corvette["color"], "can go")
corvette["run"]()
