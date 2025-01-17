first_name = 'YourMan'
last_name = 'Dank'
message = first_name + ' [' + last_name + '] is a coder'
print(message)

# While this type of formatting works, it is hard to anticipate what the outcome of a large string will be without running it, if it is not correctly formatted

first = 'YourMan'
last = 'Dank'
msg = f'{first} [{last}] is a coder '
print(msg)

# The "curly" brackets define a placeholder within which we can hold variables. The formatted string is also easier to interpret.