# .strip(), len(), .lower(), .upper(), .split()
while True:
    text= input('Input something: ')
    print(text.strip())
    print(len(text))
    print(text.lower())
    print(text.upper())
    print(text.split())
    if text == 'stop':
        break
