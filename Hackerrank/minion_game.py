vowel = 'AEIOU'

Stuart = 0
Kevin = 0

s = input()
for i in range(len(s)):
    if s[i] in vowel:
        Kevin += len(s) - i
    else:
        Stuart += len(s) - i

if Kevin > Stuart:
    print('Kevin', end=' ')
    print(Kevin)
elif Kevin < Stuart:
    print('Stuart', end=' ')
    print(Stuart)
else:
    print('Draw')
