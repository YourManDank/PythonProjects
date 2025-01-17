birth_year = input('What year were you born?')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)


# By default the birth_year will be tagged as a string. 
# We cannot subtract 2024 (an integer) from a string so we must convert the string to an integer.
# We do this with int(birth_year)
# Adding print(type(age)) allows us to see what type of variable the value is when we run the script

weight_ibs = input('What is your weight in pounds?')
weight_kg = int(weight_ibs) * 0.454
print(weight_kg)
