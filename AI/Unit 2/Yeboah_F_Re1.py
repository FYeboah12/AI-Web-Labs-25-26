import sys; args = sys.argv[1:]
idx = int(args[0])-30 # 30-39
myRegexList = [
    "/^0$|^10[01]$/", #30
    "/^[01]*$/", #31
    "/.*0$/", #32
    "/\w*[aeiou]\w*[aeiou]\w*/i", #33
    "/^0$|^1[01]*0$/", #34
    "/^[01]*110[01]*$/", #35
    "/^[\s\S]{2,4}$/", #36
    "/^\s*\d{3}[ \s]*-?[ \s]*\d{2}[ \s]*-?[ \s]*\d{4}\s*$/", #37
    "/^.*?\w*d\w*/im", #38
    "/^$|^[01]$|^0[01]*0$|^1[01]*1$/", #39-fix
]
print(myRegexList[idx])
'''
X means syntax error
E means script error
T means time out
M means missing
D means no trailing /
O means bad option
I means invalid regular expression
P means shouldn't be doing this
N means internal error
r'\ makes no \\
'''

# Frances Yeboah, P5, 2027