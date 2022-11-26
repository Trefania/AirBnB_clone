#!/usr/bin/python3
"""A Program with the class 'HBNBCommand'
containing the entry point of the command interpreter.
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
import cmd
from models import storage
from models.engine.file_storage import class_dict


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
        lst = []
        for args in line.split():
            lst.append(args)
        if len(lst) < 1:
            print("** class name missing **")
        elif lst[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            temp = eval(lst[0])()
            temp.save()
            print(temp.id)

    def do_show(self, line):
        """
        show: Prints the string representation of an instance based
         on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        -> If the class name is missing, print ** class name missing **
        (ex:$show)
        -> If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ show MyModel)
        -> If the id is missing, print ** instance id missing **
        (ex: $ show BaseModel)
        -> If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ show BaseModel 121212)
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

    def do_destroy(self, line):
        """
        destroy: Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        -> If the class name is missing, print ** class name missing **
        (ex: $ destroy)
        -> If the class name doesn’t exist, print ** class doesn't exist **
        (ex:$ destroy MyModel)
        -> If the id is missing, print ** instance id missing **
        (ex: $ destroy BaseModel)
        -> If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ destroy BaseModel 121212)
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
                del my_dict[clsid]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        all:
        Prints all string representation of all instances based or not on the
        class name.
        Ex: $ all BaseModel or $ all.
        -> The printed result must be a list of strings(like the example below)
        -> If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ all MyModel)
        """
        lst = []
        my_dict = storage.all()
        for args in line.split():
            lst.append(args)
        if len(lst) == 0:
            lex = []
            for v in my_dict.values():
                lex.append(str(v))
            print(lex)
            return
        if lst[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            lst2 = []
            for k in my_dict.keys():
                if str(k).startswith(lst[0]):
                    lst2.append(str(my_dict[k]))
            print(lst2)

    def do_update(self, line):
        """
        update: Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        -> Usage: update <class name> <id> <attribute name> "<attribute value>"
        -> Only one attribute can be updated at the time
        -> You can assume the attribute name is valid (exists for this model)
        -> The attribute value must be casted to the attribute type
        -> If the class name is missing,
        print ** class name missing ** (ex: $ update)
        -> If the class name doesn’t exist,
        print **class doesn't exist**(ex: $ update MyModel)
        -> If the id is missing,
        print ** instance id missing ** (ex: $ update BaseModel)
        -> If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ update BaseModel 121212)
        -> If the attribute name is missing,
        print ** attribute name missing **
        (ex: $ update BaseModel existing-id)
        -> If the value for the attribute name doesn’t exist,
        print ** value missing **
        (ex: $ update BaseModel existing-id first_name)
        -> All other arguments should not be used
        (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
         first_name "Betty" = $ update BaseModel 1234-1234-1234
         email "aibnb@mail.com")
        -> id, created_at and updated_at cant’ be updated.
        You can assume they won’t be passed in the update command
        -> Only “simple” arguments can be updated: string, integer and float.
        You can assume nobody will try to update list of ids or datetime
        """
        import shlex

        lst = shlex.split(line)
        my_dict = storage.all()
        try:
            cls_name = lst[0]
            if cls_name not in class_dict.keys():
                print("** class doesn't exist **")
        except Exception:
            print("** class name missing **")
            return

        try:
            ist_id = lst[1]
            clsid = f"{cls_name}.{ist_id}"
            if clsid not in my_dict.keys():
                print("** no instance found **")
        except Exception:
            print("** instance id missing **")
            return

        try:
            attr_name = lst[2]
        except Exception:
            print("** attribute name missing **")
            return

        try:
            attr_val = lst[3]
        except Exception:
            print("** value missing **")
            return

        update_dict = {}  # initialised a temporary dictionary
        # duplicating my_dict into update_dict
        for k, v in my_dict.items():
            update_dict[k] = v.to_dict()
        # appending to my duplicated dictionary.
        # Ln 184. referring to the clsid value.
        inner = update_dict[clsid]
        # Ln 186.  appending to the clsid value.
        inner[attr_name] = attr_val
        # getting all keys in the temporary dictionary.
        for k in update_dict.keys():
            class_name = update_dict[k]["__class__"]
            new_instance = update_dict[k]
            storage.new(eval(class_name)(**new_instance))
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
