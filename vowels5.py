vowels = set('aeiou')
word = input("Provide a word to search for vowels: :")
found = vowels.intersection(set(word))
for v in found:
    print(v)


