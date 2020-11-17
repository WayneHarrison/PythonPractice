import re

message = 'Call me at 415-555-1011 or at 122-310-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())
print (phoneNumRegex.findall(message))
