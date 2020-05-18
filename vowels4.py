vowels = set('aeiou')
word = input("Provide a word to search for vowels: :")

found = {

    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0

}

inter = vowels.intersection(set(word))
print(inter)


