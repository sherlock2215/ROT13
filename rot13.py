import string
def rot13(message):
    k=string.ascii_lowercase
    s=string.ascii_uppercase
    l=[]
    for i in range(len(message)):
        if message[i] in k:
            y=k.index(message[i])
            g=y+13
            e=g%26
            l.append(k[e])
        elif message[i] in s:
            l.append(s[(s.index(message[i])+13)%26])
        else:
            l.append(message[i])
    return "".join(l)
print(rot13("abc!"))