def is_palindrom(word):
    """
    Funkcja sprawdza czy podane słowo jest palindromem i zwraca wartość boolean.
    """
    letters = []
    for letter in word:
        letters += letter.lower()
    rev_letters = []
    for letter in reversed(word):
        rev_letters += letter.lower()
    return letters == rev_letters

print(is_palindrom('Kajak'))