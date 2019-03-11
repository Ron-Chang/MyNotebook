import sys

command_line = sys.argv

if len(command_line) > 1:

    for i in command_line[1:]:
        if i == "--help":
            print("the user need help")

            print("""
                ================
                help information
                ================

                -a command
                -b command
                -c command
                """)

        elif i == "-a":
            print("user call command '-a'")

        else:
            print("Error Flag")

print("")
print(command_line)
