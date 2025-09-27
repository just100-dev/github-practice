# age = 19
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are not an adult")

# marks = 0
# if marks >= 70:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# elif marks >= 40:
#     print("Grade D")
# else:
#     print("Grade F")
    
# Nested Conditionals
age = 19
citizenship = "Israeli"

if age >= 18:
    if citizenship == "Nigerian":
        print("You are Eligible to Vote")
    else:
        print("You are not Eligible to Vote due to You are not a Citizen")
else:
    print("You are not Eligible to Vote because you are not yet an Adult")