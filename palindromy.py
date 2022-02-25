def is_palindrom(word):
    """
    Funkcja sprawdza czy podane słowo jest palindromem i zwraca wartość boolean.
    """
    word = word.lower()
    return word == word[::-1]
print(is_palindrom('Kajak'))