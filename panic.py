phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.remove("D")
plist.remove("'")
plist.insert(2, " ")
plist.pop(4)
chP = plist.pop(5)
plist.insert(4, chP)

for i in range(4):
    plist.pop(6)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)