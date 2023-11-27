text = input('Enter a text to be converted: ')

letters = {
    'A':'4',
    'B':'8',
    'E':'3',
    'G':'6',
    'I':'1',
    'O':'0',
    'R':'2',
    'S':'5',
    'T':'7',
}


def converter(text):
    result = ''
    for item in text.upper():
        if item in letters.keys():
            result += letters[item]
        else:
            result += item
    return result

print(converter(text))
