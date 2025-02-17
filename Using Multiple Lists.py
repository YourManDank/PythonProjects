# Available vs unavailable items in lists:

available_toppings = ["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]

requested_toppings = ["mushrooms","french fries","extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print (f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

# This block checks the list of requested toppings against the list of available toppings and then informs the customer of any unavailabilities

# Practice:

users = ["Jamie Rooter","Henry Stoner","Edwin Belford","Jessica Daring","Oscar Howzer"]
admins = ["Oscar Howzer"]
if not users:
    print("We need some more users!")

for user in users:
    if user in admins:
        for admin in admins:
             print(f"Greetings, Administrator {admin}")
    else:
         print(f"Greetings, {user}")

# We establish two lists; users and admins, with Oscar Howzer being and admin and therfore he is an item in both lists.
# if not users: checks to see that the list us populted and executes "We need some more users!" if this statement is True.
# We then use to the for-if-else chain to prompt a different print greeting for an Admin to a regular User.

# Checking usernames:

current_users = ["Larry Lawson","Jackie Pastel","Violet Silver","Henry Ford","Rowan Sky","Mark Banham","Staci Carr"]
new_users = ["Staci Carr","Jeffrey Vallejo","Mark Banham","Harry Harris","Elizabeth De'Witt"]
for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, {new_user}, this username is taken. Please enter another.")
else:
    print("This username is available.")
