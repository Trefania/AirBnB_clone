#!/usr/bin/python3
"""A Program with the class 'HBNBCommand'
containing the entry point of the command interpreter.
"""
import models
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

    def do_create(self, line):
        """create: Creates a new instance of BaseModel, saves it (to  
        the JSON file) and prints the id. Ex: $ create BaseModel
        -> If the class name is missing, print ** class name missing ** 
        (ex: $ create)
        -> If the class name doesn’t exist, print ** class doesn't exist 
        ** (ex: $ create MyModel"""
        my_lst = []
        if not line:
            print("** class name missing **")
            return
        for args in line.split():
            my_lst.append(args)
        print(my_lst[0])
        # model1 = my_lst[0]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
