# Using multiple elif blocks to simulate discount for seniors at an amusement park:
age = 12

if age < 4:
    price = 0
elif age <18:
    price = 25
elif age >= 65:
    price = 40
else:
    price = 20

print(f'your admission cost is ${price}')
# We use the else block as a catch-all statement to set the admission price for all customers who are not infants, children or seniors. An else block is not required, it is still possible
# to use an elif block as a catch-all. Else statements can however create a vulnerability by processing malicious or irrelevant code.

# Testing multiple conditions:
requested_toppings = ['mushrooms, extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print("/n Finished making your pizza!")
# This code would not work if we used an if-elif-else block as the code would execute as soon as one test passes, where as this if block allows us to process multiple conditions


