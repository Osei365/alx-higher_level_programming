#!/usr/bin/python3
def uppercase(s):
    if s == "":
        pass
    else:
        for i in range(len(s)):
            if ord(s[i]) >= 97 and ord(s[i]) <= 122:
                ch = chr(ord(s[i]) - 32)
            else:
                ch = s[i]
            if i == len(s) - 1:
                print("{}".format(ch))
            else:
                print("{}".format(ch), end="")
