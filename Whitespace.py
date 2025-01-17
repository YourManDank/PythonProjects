# whitespace refers to any nonprinting character
# To add a tab to your printed text, use \t
print('Tabbed')
print('Without Tab')
print('\tWith Tab')

# To add a new line in a string use \n
print('Newlined')
print('Without Newline')
print('Languages \nPython \nC+ \nJavaScript')

# Combining \t and \n
print('Newlined and Tabbed')
print('\n\tPython \n\tC+ \n\tJavaScript')

# We typically strip whitespace from user inputs in order to clean the data before it is stored
favourite_language = 'Python  '
favourite_language.rstrip()
# This method will only remove whitespace from the entry in this one instance, in order to strip whitespace from the variable permanently:
favourite_language2 = 'Python  '
favourite_language2 = favourite_language2.rstrip()
# rstrip will strip from the right
# lstrip will wtrip from the left
# strip will strop from both sides

