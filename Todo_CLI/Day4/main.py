todos = list()

while True:
    user_action = str(input("Type add/edit or show or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item.capitalize())
        case 'edit':
            num = int(input('Number of the todo to edit: '))-1
            new_todo = str(input('Enter updated todo: '))
            if 0 <= num < len(todos):
                todos[num] = new_todo
                print('Updated. Here is new list: ')
                for item in todos:
                    print(item)
            else:
                print('Wrong entry.')

        case 'exit':
            break

print('Bye Bye!')
