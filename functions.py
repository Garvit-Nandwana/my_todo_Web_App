FILEPATH = "text.txt"
"""Whenever a variable is declared in capital letters, it basically means that it is a constant value and is not to be
 tempered with."""


def get_todos(filepath=FILEPATH):
    """Reads a file,
       stores the content of the file in a list and
       then returns the list."""
    with open(filepath, 'r') as file_local:
        """Writes the todo items list in the text file."""
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local2:
        file_local2.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
