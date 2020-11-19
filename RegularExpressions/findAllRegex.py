import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
ma = phoneRegex.findall('507-234-1111 120-556-9000 120-356-0989') #Allows us to search for all matches of the pattern in text.
print(ma) #Find all retrns a list not a match object in one or less groups.

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
ma = phoneRegex.findall('507-234-1111 120-556-9000 120-356-0989')
print(ma) #This will return a list of tuples of strings as there are two groups.
