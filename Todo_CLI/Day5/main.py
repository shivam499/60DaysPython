todos = list()

while True:
    user_action = str(input("Type add/edit/complete or show or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                # print(index+1, '.', item.capitalize())
                print(f"{index+1}. {item.capitalize()}")
        case 'edit':
            num = int(input('Number of the todo to edit: ')) - 1
            new_todo = str(input('Enter updated todo: '))
            if 0 <= num < len(todos):
                todos[num] = new_todo
                print('Updated. Here is new list: ')
                for index, item in enumerate(todos):
                    print(f"{index+1}. {item.capitalize()}")
            else:
                print('Wrong entry.')
        case 'complete':
            num = int(input('Number of the todo to complete: '))
            todos.pop(num-1)
            print('Deleted. Here is new list: ')
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.capitalize()}")
        case 'exit':
            break

print('Bye Bye!')
