#String Methods
spam = 'Hello World!'
spam.upper() #This will return an uppercase version of the string, whilst leaving the original unchanged.
spam         #Strings are immutable meaning they cannot be changed in place.
spam = spam.upper() #To modify a string you must reassign it.
spam.lower() #Will change a the string to lowercase.

spam.isupper() #Checks if the string is all upper case.
spam.islower() #Checks if the string is all lower case.

spam.isalpha() #Returns true boolean value if there is only letters.
spam.isalnum() #Returns true boolean value if there is only letters and numbers.
spam.isdecimal() #Returns true boolean value if there is only numbers.
spam.isspace() #Returns true boolean value if there is only whitespace.
spam.istitle() #Returns true boolean value is there is only titlecase.

','.join(['cats', 'rats', 'bats']) #Joins the strings together with the first specified character.
'Hello my name is Wayne.'.split() #Splits the string up into a list on spaces by default or a character passed into the method.
'Hello'.rjust(10) #Justifies to the right with the spaces passed. Can pass a second argument to specify character.
'Hello'.ljust(10) #Same as rjust.
'Hello'.center(20, '*')#Centers the string based on number of spaces specified. Can choose the padding character.

'         Hello'.strip() #Removes all of the whitespace.
'    Hello    '.lstrip() #removes all whitespace from left. .rstrip() Goes from the right.
'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS') #Strips the specified characters from the left and right. Center is untouched because it's surrounded by Eggs and Bacon.

'Hello There'.replace('e', 'a') #Replaces all of the specified letter with another.
