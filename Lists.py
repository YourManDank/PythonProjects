# Lists allow us to store sets of information in one place:
countries = ['France', 'Germany', 'Japan','United Kingdom']

# We can select individual items in a list:
print(countries[2])
# Remember, 0 represents the first item in the list, not 1. Meaning that this print command will print Japan, not Germany.

# We can also use the string method to apply upper/lower/title cases to the result:
print(countries[2].upper())

# Asking for the item in the list at position -1 will always return the lasst item in the list. We can  therefore get the first and last item in a list using:
print(countries[0].title())
print(countries[-1].title())
# This allows us to call items in the list by counting from either the beginning or end of the list, whichever is more convenient, which makes it easier to call
# items from large lists.

# Pulling indibvidual values from a list:
message = f'This country is not on the European continent: {countries[2].title()}'
print(message)
message_europe = f'These are the countries that are on the European continent:'
print(message_europe)
print(countries[0].title())
print(countries[1].title())
print(countries[3].title())

# Modifying items in a list (change/add/remove): the syntax for modification is the same as the syntax for accessing/calling:
motor_vehicles = ['Toyota','Honda','Ford','Bugatti','Renault']
print(motor_vehicles)

# Changing the item at position [0] in the list:
motor_vehicles[0] = 'Volkswagen'
print(motor_vehicles)

# Find the length of a list:
measurements = ['metres','centimetres','millimetres','feet','inches']
len(measurements)

# when run in >>>python, this will count the number of items as 5, not 4 - when using len() python starts the count at 1, not 0