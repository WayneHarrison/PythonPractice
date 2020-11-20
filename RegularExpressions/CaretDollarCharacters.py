import re
beginsWithRegex = re.compile(r'^Hello') #The caret(^) in this case specifies that the match must be at the start of the string.
ma = beginsWithRegex.search('Hello there!') #This would match as Hello is at the start.
print(ma.group())
ma = beginsWithRegex.search('He said "Hello there!"') #This would not as it is not at the start.
print('The string did not have "Hello" at the start:')
print(ma == None)


endsWithRegex = re.compile(r'there!$') #The dollar sign specifies the match must be at the end of the string.
ma = endsWithRegex.search('Hello there!')
print(ma.group())

allRegex = re.compile(r'^\d+$') #This means that the string must start and end with a digit or numeric character.
mo = allRegex.search('11223445678764')
print(mo.group())

atRegex = re.compile(r'.at') #. is a wildcard that will match any character.
mo = atRegex.findall('Bat Cat Sat Rat Fat')
print(mo)

dotStarRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #.* means to find all characters. In this setup it will create a group and find all characters after first and last name.
mo = dotStarRegex.findall('First Name: Wayne Last Name: Harrison')
print(mo)

dotStarQMark = re.compile(r'<(.*?)>') #This is a non greedy version of .*
mo = dotStarQMark.findall('<Hello we will crack straight into it> right now.>')
print(mo)

dotStarGreedy = re.compile(r'<.*>')
mo = dotStarGreedy.findall('<Hello we will crack straight into it> right now.>')
print(mo)

prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law.'
dotStar = re.compile(r'.*', re.DOTALL) #The secondary argument DOTALL means . will match everything including new lines.
mo = dotStar.search(prime)
print(mo.group())

vowelRegex = re.compile(r'[aeiou]', re.I) #The secondary argument .I or .INGORECASE means it will match regardless of upper or lower case.
mo = vowelRegex.findall('Albert loves to lick icecreams and get brainfreeze.')
print(mo)
