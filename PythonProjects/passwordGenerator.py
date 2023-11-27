import random
import array
import string

while True:
    length = int(input('Enter the length of your password: '))
    if length <= 16 and length >= 5:
        break
    elif length > 16:
        print('Maximum length is 16')
    else:
        print('Minimum length is 5')
NUMBERS = [i for i in string.digits]
LOWERCASE_LETTERS = [i for i in string.ascii_lowercase]
UPPERCASE_LETTERS = [i for i in string.ascii_uppercase]
exceptions = ['[', ']']
SYMBOLS = [i for i in string.punctuation if i not in exceptions]

COMBINED_LIST = NUMBERS + LOWERCASE_LETTERS + UPPERCASE_LETTERS + SYMBOLS

rand_digit = random.choice(NUMBERS)
rand_upper = random.choice(UPPERCASE_LETTERS)
rand_lower = random.choice(LOWERCASE_LETTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass  = rand_digit + rand_lower + rand_upper + rand_symbol

for i in range(length - 4):
    temp_pass += random.choice(COMBINED_LIST)
    # u is for unicode character
    # this code prevents the password from having a similar pattern everytime it is generated
    temp_pass_list = array.array('u', temp_pass) 
    random.shuffle(temp_pass_list)

password = ''
for x in temp_pass_list:
    password += x

print('Generated password:', password)
