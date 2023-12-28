feet_inches = input('Enter feet and inches: ')


def parse(feet_inches:str):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inch = float(parts[1])
    return {"feet": feet, "inch": inch}


def convert(feet, inch):
    meters = feet * 0.3048 + inch * 0.0254
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inch'])

print(f"{parsed['feet']} feet and {parsed['inch']} inches is equal to {result} meters.")

if result < 1:
    print('Kid id too small.')
else:
    print('Kid can use the slide.')
