import re
lyrics = '12 Drummers Drumming, 11 Pipers Piping 10, Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves, and 1 Partridge in a Pear Tree'

xmasRegex = re.compile(r'\d+\s\w+')
res = xmasRegex.findall(lyrics)
print(res)

#examples of defining your own regex

vowelRegex = re.compile(r'[aeiouAEIOU]') #We can define our own regex characters with square brackets in the string
res = vowelRegex.findall(lyrics) #The defined regex will pull all of the characters that match the ones we put in the square brackets.
print(res)

consonantsRegex = re.compile(r'[^aeiouAEIOU]') #This will find every character except the ones defined because of the "^"
res = consonantsRegex.findall(lyrics)
print(res)
