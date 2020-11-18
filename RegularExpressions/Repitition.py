import re

batRegex = re.compile(r'Bat(wo)?man') #The ? means that the items in the group denoted by the parentheses can appear one or zero times.
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') #Allows the area code to appear once or no times
mo = phoneRegex.search('My number is 541-654-7655')
print(mo.group())
mo = phoneRegex.search('My number is 654-7655') #The ? can be escaped with a \ so for example \? would escape it.
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man') #* means match zero or more. Can escape it with \* to find literal stars.
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowoman')
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man') #+ means one or more, so it is required in the group. Can escape with \+.
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batman')
print(mo == None)

exactRegex = re.compile(r'(ha){3}') #Matches the group to the exact amount of times as defined in the curly braces. You can define a range by adding a comma and a second higher number denoting the highest range.
mo = exactRegex.search('She started laughing like "hahaha"') # e.g {3,5} means 3-5 matches. {,5} means up to 5. {3,} means 3 or more.
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}') #Python tries to do "greedy" matches with regex. It will always take the longest possible string which will match the pattern.
mo = digitRegex.search('1234567890')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}?') #The questionmark will specify a non-greedy match but only after {3,5}. It will take the smallest possible string now instead.
mo = digitRegex.search('1234567890')
print(mo.group())
