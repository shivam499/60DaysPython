user_text = "Enter a todo:"

todos = list()
i = 0
while i < 3:
    todo = input(user_text)
    todos.append(todo)
    i += 1

print(todos)
