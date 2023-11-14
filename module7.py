#List methods
S='mumbai'

for i in range(len(S)):
    a=S[i]
    b=ord(a)
    print(f"Character:{a},Unicode code point:{b}")
s=0

for i in range(len(S)):
    a=S[i]
    b=ord(a)
    s=s+b
print(f"The sum of Unicode code points of the characters in S is {s}")
uu=[]
for i in range(len(S)):
    a=S[i]
    b=ord(a)
    uu.append(b)
print(f"The list of the Unicode code points of the characters in S is {uu}")

