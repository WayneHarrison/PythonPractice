import re
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent John gave the secret documents to Agent Nona')
print(mo)
print(namesRegex.sub('REDACTED','Agent John gave the secret documents to Agent Nona'))
#the sub method will find all occurences of the specified pattern and replace them.
namesRegex2 = re.compile(r'Agent (\w)\w*')
mo2 = namesRegex2.findall('Agent John gave the secret documents to Agent Nona')
print(mo2)
print(namesRegex2.sub(r'Agent \1','Agent John gave the secret documents to Agent Nona'))
#We can substitute things in using groups. In this case we use the first group, which will be the first letter of the names as specified in nameRegex2.
#Verbose mode.
phoneNumber = re.compile(r'''
\d\d\d      #Area code... We can add notes using multi line strings with the hash symbol.
-           #The verbose mode is what allows us by allowing us to add spaces and comments.
\d\d\d      #And adding white space too. 
-
\d\d\d\d''', re.verbose)

#We can pass multiple arguments to the compile function
#We can do this by simply doing, for example re.DOTALL | re.IGNORECASE | re.VERBOSE
#it is possible to combine them all together using the "|". 
