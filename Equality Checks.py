# Checking for equality:

vehicle = 'bmw'
vehicle == 'bmw'
# This equality check (==) will print True, as vehicle does equal bmw.
# Line 16 establishes that vechile = bmw and line 17 checks (==) for equality. This check will confirm that vehicle = 'bmw'
# and therefore print True.

# when the value of vehicle is anything other than bmw, this check will return False:
vehicle == 'audi'
# Equality checks are also case sensitive

# We can also perform a case conversion in order to make the equality check ignore case sensitivity:

automobile = 'Audi'
automobile.lower() = 'audi'

# Will return True, as we are converting the variable to lower case, this method allows us to check datasets regardless of case sensitivity

# Checking for inequality (!=):

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("No anchovies")

# (!=) effectively translates to "is not", in this circumstance Python will check to see if the value 'anchovies' matches the value 'mushrooms'.
# If the two values are not equal (!=) then the if statement is True, and the print command is executed.

# Numberical Comparison (the numbers are not given quotation marks as they are not a string, they are a numberical value):

age = 18
age == 18
# Will return True, as the values are the same.

# Checking to see if two numbers are not equal:

answer = 18
if answer != 20:
    print('that is not the correct answer')

# It is also possible to use (<) and (<=) in this operation, checking to see if the answer is lesser than (<) or lesser than / equal to (<=)

# It is also possible to check whether or not multiple conditions are True before executing an if statement:

number_0 = 22
number_1 = 18
number_0 >= 21 and number_1 >= 21
# Will return False, as while number_0 is greater than or equal to 21 - number_1 is not