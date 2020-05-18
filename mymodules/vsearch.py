def search4vowels(word: str) -> set:
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Display any vowels found in an asked-for word."""
    return set(letters).intersection(set(phrase))
