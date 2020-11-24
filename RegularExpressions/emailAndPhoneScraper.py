#! python3

import re, pyperclip

#Create regex object for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)| (\(\d\d\d\)))?            #area code (Optional)
(\s|-)            #First seperator
\d\d\d            #First 3 digits
-            #seperator
\d\d\d\d            #last 4 digits
(((ext(\.)?\s|x)            #extension (optional)
 (\d{2,5})))?      #extension Numbers (Optional)
 )
''', re.VERBOSE)

# Create regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+                        #name
@                        #@ symbol
[a-zA-Z0-9_.+]+                        #domain name
''', re.VERBOSE)
# get text off clipboard
text = pyperclip.paste()
# Extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy extracted email/phone to clipboard.

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
