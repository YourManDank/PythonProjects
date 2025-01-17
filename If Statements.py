# The following loops through a list of car names and looks for the value "bmw". Whenever the value "bmw" is printed then it is
# converted to uppercase:

cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# This if statement allows us to correctly print BMW in title case as it is an acronym while printing other brand names in
# title case
