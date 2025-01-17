# for looping:

colours = ['red','blue','green','purple','yellow']
for colours in colours:
    print(colours)

    # 3: Defines the lsit
    # 4: Commands python to pull a name from the list of colours and associate it with the variable "colours"
    # 5: Commands python to print the name that has been pulled
    # Python then repeats 4+5 for each name in the list - this sequence can be understood as:
    # "For each colour in the list of 'Colours', print the colours name"

# Formatting strings in FOR loops
magicians = ['Sam','James','Alex','George']
for magician in magicians:
    print(f"{magician.title()}, that was an amazing trick!")
    print(f"I can't wait to see your next trick, {magician.title()}")

print("Thank you everyone, that was a great show!")
# This will pring the message defined in the string after python prints each magician's name
# We define things that are included in the loop by indenting them, such as on lines 16 and 17
# To move on from the loop we simply create the next line of code without indentation so that python understands
# the new line of code is not a part of the loop

# Demonstrating an indentaion error:
cars = ['Ford','Renault','Mini','Volkswagen']
for car in cars:
print(cars)

# Python will typically automatically flag an indentation error both in the code editor and the console
# Another common error is when the writer forgets the : at the end of the for loop line, the : is used
# by python to prompt python to read the next line of code as the beginning of the loop