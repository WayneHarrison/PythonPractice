#List Methods.

spam = ['Hello', 'Hi', 'Heya']
spam.index('Heya') #Index finds the first occurence of the specified item in the list.

spam = ['Cat', 'Dog', 'Bat']
spam.append('Moose') #Append adds the specified value to the end of the list.

spam = ['Cat', 'Dog', 'Bat']
spam.insert(2, 'Chicken') #Insert adds the value to the specified index in the list.

spam = ['Cat', 'Rat', 'Bat', 'Elephant']
spam.remove('Elephant') #Deletes the specified value in the list instead of the index like with del
                        #if there are multiple it will delete the first occurance.

spam = [2, 5, 3, 1, -7]
spam.sort() #Sorts the numeric list lowest to highest.
            #Will sort words alphabetically based on the first letter.
spam.sort(reverse=True) #Sorts in reverse order instead.
                        #Cannot sort lists that are numeric and alphabetical.
                        #Capital letters are sorted first then lowercase come after.
spam.sort=(key=str.lower)#Will do true alphabetical sorting regarless of capitalisation.



