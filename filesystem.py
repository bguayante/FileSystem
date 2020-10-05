import sys

# File explorer's default location #
current_dir = "root/"

# To hold "files" and "directories" as dictionaries in a list #
fileList = []

# For creating "files" and "directories" when the touch and mkdir commands are used #


class Link:
    def __init__(self, name, parent_directory, is_directory=False):
        self.name = name
        self.parent_directory = parent_directory
        self.is_directory = is_directory

# Receive and validate user input, call relevant function #


def command_prompt():
    global command
    command = input(
        f"Current Directory: {current_dir}\nPlease choose a command: ls, mkdir, cd, touch, or exit\n$ ")
    # Check that mkdir, touch, and cd have arguments #
    if "mkdir" in command.lower() and len(command.split(" ")) <= 1:
        print("Error: the mkdir command requires an argument. Try mkdir <dir_name>.")
        command_prompt()
    elif "touch" in command.lower() and len(command.split(" ")) <= 1:
        print("Error: the touch command requires an argument. Try touch <file_name>.")
        command_prompt()
    elif "cd" in command.lower() and len(command.split(" ")) <= 1:
        print("Error: the cd command requires an argument. Try cd <dir_name>.")
        command_prompt()
    # Calling functions according to user input #
    elif "ls" in command.lower():
        ls()
    elif "mkdir" in command.lower():
        mkdir()
    elif "cd" in command.lower():
        cd()
    elif "touch" in command.lower():
        touch()
    elif "exit" in command.lower():
        sys.exit("Goodbye!")
    else:
        print("Invalid command.")
        command_prompt()

# FUNCTIONS #


def ls():
    # Checks that directory has contents and prints them #
    print("Directory contents:")
    n = 0
    for x in fileList:
        if x["parent_directory"] == current_dir:
            n += 1
            print(x["name"])
    if n < 1:
        print("This directory is empty.")
    command_prompt()


def mkdir():
    # Checks for potential duplicates and creates directories #
    global command
    new_dir = command.lower().split()[1]
    for x in fileList:
        if new_dir + "/" == x["name"] and current_dir == x["parent_directory"]:
            print(
                f"A directory called '{new_dir}' already exists in this location.")
            command_prompt()
    fileList.append(Link(new_dir + "/", current_dir, True).__dict__)
    print(f"Directory '{new_dir}' has been created.")
    command_prompt()


def cd():
    global current_dir
    dir = command.lower().split()[1]
    # Navigating "up" a level. Goes no further than "root/" #
    if dir == "..":
        if current_dir == "root/":
            print("You are in the root directory. You may go no deeper.")
        else:
            # Split directory path by "/", delete last directory, rejoin directory path with "/" #
            current_dir = current_dir.split("/")
            del current_dir[-2]
            current_dir = "/".join(current_dir)
        command_prompt()
    elif dir:
        n = 0
        for x in fileList:
            # Check that subdirectory exists and is in current directory #
            if dir in x["name"] and x["is_directory"] and current_dir == x["parent_directory"]:
                n += 1
        if n:
            current_dir = current_dir + dir + "/"
        # Otherwise, throw error #
        else:
            print("Directory not found.")
    command_prompt()


def touch():
    # Checks for potential duplicates and creates files #
    global command
    new_file = command.lower().split()[1]
    for x in fileList:
        if new_file == x["name"] and current_dir == x["parent_directory"]:
            print(
                f"A file named '{new_file}' already exists in this location.")
            command_prompt()
    fileList.append(Link(new_file, current_dir).__dict__)
    print(f"File '{new_file}' has been created.")
    command_prompt()


if __name__ == '__main__':
    command_prompt()
