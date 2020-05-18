phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

tapStr = plist[1:3:1]
for e in plist[5:3:-1]:
    tapStr.append(e)

for e in plist[7:5:-1]:
    tapStr.append(e)

new_phrase = ''.join(tapStr)
print(plist)
print(new_phrase)