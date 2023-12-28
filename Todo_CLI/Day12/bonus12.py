feet_inches = input('Enter feet and inches: ')


def convert(feet_inch):
    parts = feet_inch.split(' ')
    feet = float(parts[0])
    inch = float(parts[1])

    meters = feet*0.3048 + inch*0.0254

    return meters


result = convert(feet_inches)

if result < 1:
    print('Kid id too small.')
else:
    print('Kid can use the slide.')
