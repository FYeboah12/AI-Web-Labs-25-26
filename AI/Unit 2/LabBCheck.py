import re

#45: adj diff vowel
pattern = "\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*"
match = re.match(pattern,"sean")
print(45,match)

#46: dont include 110
pattern = "^[01]*(?:(^110))[01]*$"
match = re.match(pattern,"110")
print(46,match)

#47: at most one 'a'
pattern = "^([bc]*a?[bc]*)$"
match = re.match(pattern,"baca")
print("47", match)

#48: even number of 'a'
#pattern = "([bc]*|(a*)?[bc]*\1?[bc]*\1?)"
pattern = "[bc]*a([bc]*a)*[bc]+"
match = re.match(pattern,"abc")
print(48, match)

#49: positive even base 3
pattern = "^([02]*1[02]*)*\1$"
match = re.match(pattern,"10000100")
print(match)
