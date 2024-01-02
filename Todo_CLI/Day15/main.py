# Today we are working on files
# Added functionality to read/write todos from file
# Added custom function for code reliability

# from functions import read_file, write_file
import functions
import time

"""
Other way to import functions only

and write every method like functions.read_file() or functions.write_file()
"""

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

try:

    while True:
        user_action = str(input("Type add/edit/complete or show or exit: ")).strip()

        if user_action.startswith('add') or user_action.startswith('more') or user_action.startswith('new'):
            todo = user_action[4:] + "\n"

            todos = functions.read_file()

            todos.append(todo)

            functions.write_file(todos)

        elif user_action.startswith('show'):
            todos = functions.read_file()

            if len(todos) > 0:
                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item.strip('\n').capitalize()}")
            else:
                print("You don't have any todo to work on. Add todos or Enjoy the day!!")

        elif user_action.startswith('edit'):

            try:
                num = int(user_action[5:]) - 1
                new_todo = str(input('Enter updated todo: ')) + "\n"

                todos = functions.read_file()

                if 0 <= num <= len(todos):
                    todos[num] = new_todo.capitalize()

                    functions.write_file(todos)

                    print('Updated. Here is new list: ')
                    for index, item in enumerate(todos):
                        print(f"{index + 1}. {item.strip('\n').capitalize()}")
                else:
                    print('Wrong entry.')
            except ValueError:
                print('Wrong Value entered. Enter the todo Number to edit.')

        elif user_action.startswith('complete') or user_action.startswith('done'):
            num = int(user_action.split(' ')[1])

            try:
                todos = functions.read_file()

                deleted_todo = todos.pop(num - 1).strip('\n')

                functions.write_file(todos)

                print(f'{deleted_todo} todo Completed. Here is new list: ')

                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item.strip('\n').capitalize()}")

            except IndexError:
                print('You have entered a wrong Todo Id.')
                continue

        elif user_action.startswith('exit'):
            print('Bye Bye!')
            break
        else:
            print('Command not found.')

except KeyboardInterrupt:
    print("Program closed forcefully.")
    pass
