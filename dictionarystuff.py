myCat = {'size': 'Fat', 'colour': 'Orange', 'disposition': 'Quiet'} #Dictionary datatypes are opened with curly braces.
#The keys and values are seperated by a colon, and new pairs are denoted by the comma.
myCat['size'] #This will allow you to refer to the value stored by that key.
#It is possible to concatenate these strings like below.
'My cat is very ' + myCat['size'] + '.'
#Items in a dictionary are unordered and when compared the values can be in any order, unlike a list.
#It is possible to check if keys are in with the in and not in operators.
#There are three methods you can use to look into a dictionary. keys(), values(), and items().
#keys() returns the keys within the dictionary, values() the values, and items() returns both keys and values.
list(myCat.keys()) #this would return keys for example.
#The get() method provides a fallback incase there is no value. E.g:
myCat.get('colour', 'Colour is not stored')
#It looks for the colour keys, if not it defaults to the second value.
#The opposite of the get method is the setdefault() method.
#It will check the dictionary for the key and if it doesn't exist it will set it to the default value.
myCat.setdefault('age', 5)
