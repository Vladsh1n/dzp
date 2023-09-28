mirrored_symbols_in_self = [
    'A', 'H', 'I', 'M', 'O', 'T',
    'U', 'V', 'W', 'X', 'Y', '1',
    '8'
]
mirrored_symbols = {
    'E' : '3',
    'J' : 'L',
    'S' : '2',
    'Z' : '5',
    '3' : 'E',
    'L' : 'J',
    '2' : 'S',
    '5' : 'Z'
    }
string = input('')
def isRegPal():
    counter = 1
    isRegPalindrome = False
    for k in string:
        if k not in mirrored_symbols_in_self:
            counter = 0
    for i in range(0, len(string)):
        if string[i] == string[-1-i] and counter == 0:
            isRegPalindrome =  True
        else:
            isRegPalindrome = False
    return(isRegPalindrome)
def isMirString():
    isMirroredString = False
    for i in range(0, len(string)):
        first = string[i]
        last = string[-1-i]
        for z in mirrored_symbols:
            if first == z:
                if last == mirrored_symbols[z]:
                    isMirroredString = True
                else:
                    isMirroredString = False
    return(isMirroredString)
def isMirPalindrome():
    isMirroredPalindrome = False
    for i in range(0, len(string)):
        first = string[i]
        last = string[-1-i]
        if first in mirrored_symbols_in_self:
            if first == last:
                isMirroredPalindrome = True
            else:
                isMirroredPalindrome = False
    return(isMirroredPalindrome)

if isRegPal():
    print('It is regular palindrome!')
elif isMirString():
    print('It is mirrored string!')
elif isMirPalindrome():
    print('It is mirrored palindrome!')
else:
    print('It isn\'t palindrome!')