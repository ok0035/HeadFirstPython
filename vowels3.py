vowels = set('aeiou')
word = input("Provide a word to search for vowels: :")
found = {

    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0

}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    if v is not 0:
        print(k, 'was found', v, 'time(s).')
