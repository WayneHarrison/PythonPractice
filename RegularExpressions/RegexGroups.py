import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #Groups are denoted by parentheses. You can escape parentheses if you need to find them using \
mo = phoneNumRegex.search('My phone number is 456-213-9543')
print(mo.group(1)) #Gets the first group and prints it.
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My phone number is (456) 213-9543')
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #It is possible to search multiple suffixes using the pipe character.
mo = batRegex.search('Batmobile lost a wheel') 
print(mo.group())
