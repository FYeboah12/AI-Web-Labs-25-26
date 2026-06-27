import sys; args = sys.argv[1:]
idx = int(args[0])-50 # 50-59
myRegexList = [
 r"/(\w)+\w*\1\w*/i", #50
 r"/(\w)+\w*\1\w*\1\w*\1\w*/i", #51
 r"/^[01]$|^([01])[01]*\1$/",#52 same 01 10
 r"/\b(?=\w*cat)\w{6}\b/i",#53
 r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i",#54
 r"/\b(?!\w*cat)\w{6}\b/i",#55
 r"/\b(?!\w*(\w)\w*\1)\w+\b/i",#56
 r"/^((?!10011)[01])*$/",#57
 r"/\w*([aeiou])(?!\1)[aeiou]\w*/i",#58
 r"/^((?!1.1)[01])*$/"#59
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