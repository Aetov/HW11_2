userinput = input()
def capital_letters():
    """Это функция переводит всё слово
        в заглавные буквы, которое ввел
        пользователь, при помощи метода str.upper
    """
    return str.upper(userinput)

print(capital_letters())

def first_capital_letters():
    """Это функция переводит только первую букву
        из слова, которое ввел
        пользователь, при помощи метода str.capitalize
    """
    return str.capitalize(userinput)

print(first_capital_letters())
