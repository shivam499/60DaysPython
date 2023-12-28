try:
    length = float(input('Enter rectangle length: '))
    width = float(input('Enter rectangle width: '))
    if length == width:
        exit('It looks like a square.')
    area = width * length
    print(area)
except ValueError:
    print('Please enter a number: ')
