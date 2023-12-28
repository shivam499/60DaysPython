# Todo we are working on files
# Added functionality to read/write todos from file


while True:
    user_action = str(input("Type add/edit/complete or show or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")+"\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            # Adding todos into file
            file = open('todos.txt', 'w')
            file.writelines(todos)

            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            if len(todos) > 0:
                for index, item in enumerate(todos):
                    # print(index+1, '.', item.capitalize())
                    print(f"{index + 1}. {item.capitalize()}")
            else:
                print("You don't have any todo to work on. Add todos or Enjoy the day!!")
        case 'edit':
            num = int(input('Number of the todo to edit: ')) - 1
            new_todo = str(input('Enter updated todo: '))+"\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            if 0 <= num < len(todos):
                todos[num] = new_todo

                file = open('todos.txt', 'w')
                file.writelines(todos)
                file.close()

                print('Updated. Here is new list: ')
                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item.capitalize()}")
            else:
                print('Wrong entry.')

        case 'complete':
            num = int(input('Number of the todo to complete: '))

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.pop(num - 1)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

            print('Deleted. Here is new list: ')
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.capitalize()}")
        case 'exit':
            break

print('Bye Bye!')
