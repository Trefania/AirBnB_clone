#!/usr/bin/python3
"""A Program with the class 'HBNBCommand'
containing the entry point of the command interpreter.
"""
from models.base_model import BaseModel
from models import storage
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
        ** (ex: $ create MyModel)"""

        for args in line.split():
            if args is None:
                print("** class name missing **")
            elif args not in class_dict.keys():
                print("** class doesn't exist **")
            else:
                temp = eval(args)()
                temp.save()
                print(temp.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        -> If the class name is missing, print ** class name missing ** (ex: $ show)
        -> If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
        -> If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        -> If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        lst = []
        for args in line.split():
            lst.append(args)
        if len(lst) < 1:
            print("** class name missing **")
        elif len(lst) < 2:
            print("** instance id missing **")
        elif lst[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            cls_name = lst[0]
            ist_id = lst[1]
            clsid = f"{cls_name}.{ist_id}"
            my_dict = storage.all()
            if clsid in my_dict.keys():
                print(my_dict[clsid])
            else:
                print("** no instance found **")

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
