# If statements with lists allow for us to manage changing conditions, such as a restaurant running out of a particular item on the menu.
# A scenario in which a Pizzeria displays a message each time a topping is added to a customer's pizza, a loop is used to announce each topping:

requested_toppings = ['mushrooms, green peppers, extra cheese']

for requested_topping in requested_toppings:
    print('Adding {requested_topping}.')

print('Finished making your pizza!')

# If the pizzeria runs out of an item:

toppings = ['mushrooms, green peppers, extra cheese']
for topping in toppings:
    print('Adding your {toppings}!')
    if topping == 'green peppers':
        print('Sorry! We are out of green peppers')
    else:
        print(f'Adding {topping}.')

    print("\nFinished making your pizza!")
# This block checks to see if the customer has ordered a topping that is out of stock.

#Checking that a list is not empty:

available_toppings = []

if available_toppings:
    for available_topping in available_toppings:
        print(f'Adding {available_topping}.')
    print('\nFinished making your pizza!')

else:
    print('Are you sure you want a plain pizza?')