name = 'Sean Morgan'
print('basic up/lower')
print(name.upper())
print(name.lower())
# In some cases we may want to represent that first and last name with seperate variables and them combine them when printing:

first_name = 'Sean'
last_name = 'Morgan'
full_name = f'{first_name} {last_name}'
# f'{value}{value2}{value3}' "f" stands for format, meaning a formatted string, putting values into the {braces} makes it easier to visualise what the formatted string does
# at a glance without having to run the programme

print('Using formatted string method')
print(full_name.upper()) 
print(first_name.lower())
print(last_name.lower())

print("Using .title to ensure user's name is capitalised")
print(f'Hello, {full_name.title()}!')
# adding the .title() method changes the user's response to be capitalised


# we can also use f strings to compose complete messages using a combination of the 'written word' and '{values}':
print(f'Hello {full_name} how are you?')
# It is also a good idea to convert user responses into lower case so that they can be stored and scraped easier by data  analysis systems

#We can also assign our response message to a unique variable in order to make the final print  call easier to handle:

response = f'Hello, {full_name.title()}!'
print(response)