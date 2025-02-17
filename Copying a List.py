# Make a slice that includes the entire index of a list:
my_foods = ['Pizza','Pasta','Rice','Chicken','Broccoli','Pork','Beef','Cheesecake']
friends_foods = my_foods[:]

print("My Favourite foods are")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friends_foods)

# To prove that the list has been correctly copied we will append a new item to each list and then print them both:

my_foods.append("Yoghurt")
friends_foods.append("Cake")
print(my_foods)
print(friends_foods)

# We cannot use an = to make a new list, as an = will establish both lists as a constant, meaning that will permanently contain the same items
# We must therefore slice an entire list in order to create an editable copy