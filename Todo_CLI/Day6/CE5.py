file = open('files/members.txt', 'r')
members = file.readlines()
file.close()

user = input('Add a new member: ')+"\n"
members.append(user)

file = open('files/members.txt', 'w')
file.writelines(members)
file.close()

print(members)