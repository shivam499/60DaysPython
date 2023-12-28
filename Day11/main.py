# Today we are working on files
# Added functionality to read/write todos from file
# Added custom function for code reliability


def read_file():
    with open('todos.txt', 'r') as file:  # with context manager
        return file.readlines()


def write_file():
    with open('todos.txt', 'w') as file:  # with context manager
        file.writelines(todos)


while True:
    user_action = str(input("Type add/edit/complete or show or exit: ")).strip()

    if user_action.startswith('add') or user_action.startswith('more') or user_action.startswith('new'):
        todo = user_action[4:] + "\n"

        todos = read_file()

        todos.append(todo)

        write_file()

    elif user_action.startswith('show'):
        todos = read_file()

        # list comprehension
        # new_todo = [item.strip('\n') for item in todos]

        if len(todos) > 0:
            for index, item in enumerate(todos):
                # print(index+1, '.', item.capitalize())
                print(f"{index + 1}. {item.strip('\n').capitalize()}")
        else:
            print("You don't have any todo to work on. Add todos or Enjoy the day!!")

    elif user_action.startswith('edit'):

        try:
            num = int(user_action[5:]) - 1
            new_todo = str(input('Enter updated todo: ')) + "\n"

            todos = read_file()

            if 0 <= num <= len(todos):
                todos[num] = new_todo.capitalize()

                write_file()

                print('Updated. Here is new list: ')
                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item.strip('\n').capitalize()}")
            else:
                print('Wrong entry.')
        except ValueError:
            print('Wrong Value entered. Enter the todo Number to edit.')

    elif user_action.startswith('complete'):
        num = int(user_action[9:])

        try:
            todos = read_file()

            deleted_todo = todos.pop(num - 1).strip('\n')

            write_file()

            print(f'{deleted_todo} todo Completed. Here is new list: ')

            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip('\n').capitalize()}")

        except IndexError:
            print('You have entered a wrong Todo Id.')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command not found.')

print('Bye Bye!')
