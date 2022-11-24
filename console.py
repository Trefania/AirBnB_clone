#!/usr/bin/python3
"""A Program with the class 'HBNBCommand'
containing the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A Command Interpreter."""
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """Exits Program"""
        return True

    def do_quit(self, arg):
        """Quit Function to Exit the Program."""
        quit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
