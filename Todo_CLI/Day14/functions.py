def read_file(filename='todos.txt'):
    with open(filename, 'r') as file:  # with context manager
        return file.readlines()


def write_file(todo_val, filename='todos.txt'):
    with open(filename, 'w') as file:  # with context manager
        file.writelines(todo_val)


if __name__ == "__main__":
    print("Hello")
    print(read_file())
