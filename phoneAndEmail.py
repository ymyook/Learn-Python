#!python3
#phoneAndEmail.py

import pyperclip, re

'''
(1)r means don't escape characters.
(2)? means preceding expression is optional
(3)| is 'or'
(4)\s is space

'''
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)


'''
(1)a-z inside character class is a range.
(2)each character inside class is allowed.
(3)+ is at least once. It is not optional- must appear at least once.
(4){2,4} denote a range from 2 to 4.
'''

emailRegex = re.compile(r'''(
    [a-zA-z0-9._%+-]+
    @
    [a-zA-z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

    
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
