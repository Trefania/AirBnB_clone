#!/usr/bin/python3
"""A Program with the class 'HBNBCommand'
containing the entry point of the command interpreter.
"""
from models.base_model import BaseModel
import cmd

class_dict = {"BaseModel": BaseModel}


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
        If the class name is missing, print ** class name missing **
        (ex: $ create)
        If the class name doesn’t exist, print ** class doesn't exist
        ** (ex: $ create MyModel"""

        for args in line.split():
            if args is None:
                print("** class name missing **")
            elif args not in class_dict.keys():
                print("** class doesn't exist **")
            else:
                temp = eval(args)()
                temp.save()
                print(temp.id)
    # def do_create(self, line):
    #     """create: Creates a new instance of BaseModel, saves it (to
    #     the JSON file) and prints the id. Ex: $ create BaseModel
    #     -> If the class name is missing, print ** class name missing **
    #     (ex: $ create)
    #     -> If the class name doesn’t exist, print ** class doesn't exist
    #     ** (ex: $ create MyModel"""
    #     class_dict = {"BaseModel": BaseModel}
    #     my_lst = []
    #     if not line:
    #         print("** class name missing **")
    #         return
    #     for k, v in class_dict.items():
    #         if line == k:
    #             new_instance = v()
    #             print(new_instance.id)
    #         else:
    #             print("** class doesn't exist**")
    #             # for args in line.split():
    #             #     my_lst.append(args)
    #             # # print(my_lst[0])
    #             # model1 = my_lst[0]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
