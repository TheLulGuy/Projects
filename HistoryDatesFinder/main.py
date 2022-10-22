import sys
from pprint import pformat

def extract():
    with open('dates.txt', 'r') as f:
        lines = f.readlines()
        dict = {}
        for item in lines:
            # Remove trailing whitespace
            lines[lines.index(item)] = item.rstrip()
        
        # Split the text into the info and date
        for item in lines:
            a, b = item.split('-')
            dict[a.rstrip()] = b.lstrip()

        # Order dictionary according to date
        dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}    
    
    return dict

def update():
    dictionary = extract()
    with open('dictionary.py', 'w') as f:
        f.write(f'dictionary = {pformat(dictionary)}')

def search():
    dictionary = extract()
    while True:
        info = input('Enter the event name: ')
        if info == 'all':
            for item, date in dictionary.items():
                print(item, '-', date)
        elif info == 'q':
            break
        else:
            for item, date in dictionary.items():
                if info in item:
                    print(item, '-', date)

if __name__ == '__main__':
    update()
    search()

    
# try:
#     i = sys.argv[1]
#     if i == 'update':
#         update()
#         print('Updated')
#     elif i == 'search':
#         search()
#     else:
#         raise KeyboardInterrupt
# except IndexError:
#     print('Enter something bruh')
#     exit()
# except KeyboardInterrupt:
#     print('Invalid input')
#     exit()



