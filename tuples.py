my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(my_tuple)

another_tup = 5, 6, 7, 8, 9, 10, 11, 12
# print(another_tup)

# Single Element Tuple
sing_tup = (9,)
# print(sing_tup)

# Converting from List to Tuple
# print(animals_tup)

# Accessing Elements
# print(animals_tup[2])

# Tuple Slicing
# print(animals_tup[1:4])

# new_animaltup = animals_tup + ("Buffalo", "Dog")
# print(new_animaltup)

# count() Method
# print(animals_tup.count("Lion"))

# index() method
# print(animals_tup.index("Tiger"))

# Repetition
# animals_tup = tuple(["Rabbit", "Bull", "Lion", "Tiger", "Leopard", "Cheetah", "Lion"])
# rep_tuples = animals_tup * 3
# print(rep_tuples)

# Membership Testing
# print("Goat" in animals_tup)

# Unpacking
my_family = ("Eze", "Eunice", "Ben", "Richard", "Martha", "Aisha")
dad, mum, elder_bro, *rest = my_family
# print(rest)

# Nested Tuples
numbers = (1, 2, 3, (4, 5, 6), 7, 8, 9)
print(numbers[3][1])

str1 = "Hello"
new_tup = tuple(str1)
print(new_tup)
