FILEPATH ="todos.txt"

def get_todos(filepath = FILEPATH):
    """Read the text file and return
    to-do list items
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg ,filepath = FILEPATH):
    """Write to-do item list in the text file"""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print("Hello it starts from here")
    print(get_todos())