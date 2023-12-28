# Strong password

result = dict()

password = input('Enter the password: ')

length = False
if len(password) >= 8:
    length = True

upper_case = False
for ch in password:
    if ch.isupper():
        upper_case = True

digit = False
for ch in password:
    if ch.isdigit():
        digit = True

result['length'] = length
result['upper-case'] = upper_case
result['digit'] = digit

print(result)

if all(result):
    print("Strong Password.")
else:
    print("Weak password.")
