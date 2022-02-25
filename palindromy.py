def is_palindrom(word):
    """
    Funkcja sprawdza czy podane słowo jest palindromem i zwraca wartość boolean.
    """
    return word.lower()==word[::-1].lower()

print(is_palindrom('Kajak'))