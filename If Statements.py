# The following loops through a list of car names and looks for the value "bmw". Whenever the value "bmw" is printed then it is
# converted to uppercase:

cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# This if statement allows us to correctly print BMW in title case as it is an acronym while printing other brand names in
# title case. If the parameter defined by the if statement proves Flase then Python ignores the code following the if statement.

# A (=) is a statement
# (==) is a question - "is this equal to?"

# Simple if statements:

age = 19
if age >= 18:
    print("Congratulations, you are old enough to vote!")

# if-else statements:

voter_age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are not old enough to vote yet.")
    print("We value your vote, please use it when you are old enough.")

# The if-elif-else chain:
# This chain allows us to test more than two situations, Python will run each conditional test in chronological order until one passes.
# Once a test passes, it skips the remainder of the tests.

# Admission test:
# . Admission for anyone under the age of 4 is free.
# . Admission for anyone between the ages of 4 and 18 is $25.
# . Admission for anyone age 18 or older is $40.

admission_age = 12
if admission_age <4:
    print("Your admission is free!")
elif age <18:
    print("You admission costs $25.")
else:
    print("Your admission cost is $40")

# Rather than putting the $ symbol in the print element we can use a formatted string to establish it after:

ages = 12
if age <4:
    price = 0
elif age <18:
    price = 25
else:
    price = 40
print (f"Your admission cost is ${price}")