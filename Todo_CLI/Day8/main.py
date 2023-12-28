# Today we are working on files
# Added functionality to read/write todos from file
# Added the file read/write code in edit section before taught in Day 8


while True:
    user_action = str(input("Type add/edit/complete or show or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:  # with context manager
                todos = file.readlines()

            todos.append(todo)

            # Adding todos into file
            with open('todos.txt', 'w') as file:  # with context manager
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:  # with context manager
                todos = file.readlines()

            # list comprehension
            # new_todo = [item.strip('\n') for item in todos]

            if len(todos) > 0:
                for index, item in enumerate(todos):
                    # print(index+1, '.', item.capitalize())
                    print(f"{index + 1}. {item.strip('\n').capitalize()}")
            else:
                print("You don't have any todo to work on. Add todos or Enjoy the day!!")
        case 'edit':
            num = int(input('Number of the todo to edit: ')) - 1
            new_todo = str(input('Enter updated todo: ')) + "\n"

            with open('todos.txt', 'r') as file:  # with context manager
                todos = file.readlines()

            if 0 <= num <= len(todos):
                todos[num] = new_todo

                with open('todos.txt', 'w') as file:  # with context manager
                    file.writelines(todos)

                print('Updated. Here is new list: ')
                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item.strip('\n').capitalize()}")
            else:
                print('Wrong entry.')

        case 'complete':
            num = int(input('Number of the todo to complete: '))

            with open('todos.txt', 'r') as file:  # with context manager
                todos = file.readlines()
            if 0 <= num <= len(todos):
                deleted_todo = todos.pop(num - 1).strip('\n')

                file = open('todos.txt', 'w')
                file.writelines(todos)
                file.close()

                print(f'{deleted_todo} todo Completed. Here is new list: ')

                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item.strip('\n').capitalize()}")
            else:
                print("Wow, you had completed all the todos. Add todos or Enjoy the day!!")
        case 'exit':
            break

print('Bye Bye!')
