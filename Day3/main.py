todos = list()

while True:
    user_action = str(input("Type add or show or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':  # | 'display':
            for item in todos:
                print(item.capitalize())
        case 'exit':
            break
        # case _:
        #    print('You have entered the wrong command!!')

print('Bye Bye!')
