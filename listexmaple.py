# count_chandra = [1,2,3,4,5,6]
countries = ['india', 'europe', 'delhi', 'gujrat']
change = ['india', 3, 'delhi', 2]

# looping in multilist
# for a, b, c in zip(count_chandra, countries, change):
#     print(f"this is count {a}")
#     print(f"this country of type: {b}")
#     print(f"i got {c}")

#enumerate:

# for i, (b, c) in enumerate (zip(countries, change)):
#     print(f"this is count {i}")
#     print(f"this country of type: {b}")
#     print(f"i got {c}")
def my_loop_function (my_contries, my_change):
    for i, (b, c) in enumerate (zip(my_contries, my_change)):
        print(f"this is count {i}")
        print(f"this country of type: {b}")
        print(f"i got {c}")
    return

my_loop_function(countries, change) 


# for number in count_chandra:
#     print(f"this is count {number}")

# for country in countries:
#     print(f"this country of type: {country}")

# for i in change:
#     print(f"i got {i}")

# elements = []

# for i in range (0,7):
#     print(f"adding {i} to the list")
#     elements.append(i)

# for i in elements:
#     print(f"elements was:{i}")



