#самый частый символ


def p(s):
    count=dict()
    mx=0
    mx_char=''
    for c in s:
        if c not in count:
            count[c]=0
        count[c]+=1
        if count[c]>mx:
            mx=count[c]
            mx_char=c
    return mx_char
print(p('aabbbbb'))