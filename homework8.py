# Homework #8
# Note-taking program

import os

filename = input("Please enter the filename: ")
# Here we check if the file exists
if os.path.isfile("./" + filename):
    print("Looking for file {}...".format(filename))
    print("Found it!")
    action = input(
        "What would you like to do with the file?\nPossible actions are: read, delete, append, replace\n")
    if action == "read":
        print("The content of the file:")
        with open(filename, "r") as read_file:
            print(read_file.read())
    elif action == "append":
        text = input("Please enter your note: ")
        with open(filename, "a") as append_file:
            append_file.write(text + "\n")
    elif action == "delete":
        os.remove("./" + filename)
        print("{} have been deleted.".format(filename))
        with open(filename, "w") as write_file:
            write_file.write("")
    elif action == "replace":
        line_num = int(
            input("Please enter the line number for the replacement: "))
        text = input("Please enter your note: ")
        with open(filename, "r") as read_file:
            lines = read_file.readlines()
        with open(filename, "w") as write_file:
            for idx, line in enumerate(lines):
                if idx == line_num - 1:
                    print("Line num {} needs to be replaced!".format(line_num))
                    write_file.write(text + "\n")
                else:
                    print("Writing \"{}\"".format(line))
                    write_file.write(line)

    else:
        print("Sorry, unrecognized action 😢")
else:
    print("Nope, this file does not exist, I'm going to create it for you! 😄")
    text = input("Please enter your note: ")
    with open(filename, "w") as write_file:
        write_file.write(text + "\n")
