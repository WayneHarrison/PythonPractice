print('Hello'.isalpha()) #Checks if all characters are alphabetical.
print('Hello123'.isalnum()) #Checks if characters are both numeric and alphabetical.
print('123'.isdecimal()) #Checks if all caharacters are numbers.
print('    '.isspace()) #Checks for whitespaces.
print('Hello'.istitle()) #Checks for titlecase.
print('HELLO'.isupper()) #Checks if all are uppercase.
print('hello'.islower()) #Checks if everything is lowercase.
print('Hello'.startswith('H')) #Checks if string starts with specified letter/string.
print('Hello'.endswith('o')) #Checks if string ends with specified letter/string.
print(', '.join(['Mom','Dad','Sister'])) #Joins the list of strings together with the specified character.
print('My name is Wayne'.split()) #Splits the string on white space or specified character creates a list.
print('Hello'.rjust(10)) #Right justify. Number is how many characters, so enough spaces to make the string 10 characters long.
print('Hello'.ljust(10)) #Left Justify. Same as above.
print('Hello'.rjust(10, '*')) #Right justify with custom character padding.
print('Hello'.center(10)) #Centers the text within 10 characters. Can add custom fill characters.
print('Hello    '.strip()) #Removes all white spaces. lstrip removes from left rstrip from right.
print('lllHellolll'.strip('l')) #Removes specific character from edges.
print('Hello'.replace('l', 'w')) #Replaces specifed character with another.
