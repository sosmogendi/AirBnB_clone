#!/usr/bin/python3
"""
This module defines the HBNBCommand class that provides the command interpreter
for the AirBnB clone project.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines the command interpreter for the AirBnB clone project.
    It inherits from the cmd.Cmd class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program at EOF
        """
        return True

    def emptyline(self):
        """
        Empty line does nothing
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
