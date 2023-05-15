#!/usr/bin/python3

'''
    a program called console.py that contains the entry
    point of the command interpreter
'''
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def isfloat(args):
    try:
        float(args)
        return True
    except ValueError:
        return False


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    cls_list = [
            "BaseModel", "User", "Place", "State",
            "City", "Amenity", "Review"
            ]

    def do_EOF(self, line):
        """to exit the program\n"""
        return True

    def do_quit(self, line):
        """to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything\n"""
        pass

    def do_create(self, argss):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if not argss:
            print("** class name missing **")
            return
        else:
            args = argss.split()
            if len(args) != 1:
                print("** class doesn't exist **")
                return
            elif len(args) == 1 and args[0] not in self.cls_list:
                print("** class doesn't exist **")
                return
            else:
                inst = eval(args[0])()
                inst.save()
                print(inst.id)

    def do_show(self, argss):
        """
        Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.

            inst_rep: variable for string representation of an instance
            object_store: __objects{} dict gotten from the FileStorage class
        """
        if not argss:
            print("** class name missing **")
        else:
            args = argss.split()
            if len(args) > 2:
                # print("fail")
                return
            else:
                if len(args) == 1 and args[0] not in self.cls_list:
                    print("** class doesn't exist **")
                    return
                if len(args) == 1 and args[0] in self.cls_list:
                    print("** instance id missing **")
                    return
                if len(args) == 2 and args[0] in self.cls_list:
                    object_store = models.storage.all()
                    key = args[0]+"."+args[1]
                    inst_rep = object_store.get(key)
                    if inst_rep:
                        print(inst_rep)
                    else:
                        print("** no instance found **")

    def do_destroy(self, argss):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not argss:
            print("** class name missing **")
        else:
            args = argss.split()
            if len(args) > 2:
                # print("fail")
                return
            else:
                if len(args) == 1 and args[0] not in self.cls_list:
                    print("** class doesn't exist **")
                    return
                if len(args) == 1 and args[0] in self.cls_list:
                    print("** instance id missing **")
                    return
                if len(args) == 2 and args[0] in self.cls_list:
                    object_store = models.storage.all()
                    key = args[0]+"."+args[1]
                    if key in object_store.keys():
                        del object_store[key]
                        models.storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, argss):
        """
        Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all
        """
        if not argss:
            object_store = models.storage.all()
            item_str = []
            for value in object_store.values():
                val_str = f"\"{value}\""
                item_str.append(val_str)
            result = ", ".join(item_str)
            print(f"[{result}]")

        else:
            args = argss.split()
            if len(args) == 1 and args[0] not in self.cls_list:
                print("** class doesn't exist **")
                return
            else:
                object_store = models.storage.all()
                item_str = []
                for key in object_store:
                    if isinstance(object_store[key], eval(args[0])):
                        value = object_store[key]
                        val_str = f"\"{value}\""
                        item_str.append(val_str)
                result = ", ".join(item_str)
                print(f"[{result}]")

    def do_update(self, argss):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        args[1] = BaseModel
        args[2] = id i.e. 1234-1234-1234
        args[3] = attribute name i.e. email
        args[4] = attribute value i.e. "aibnb@mail.com"
        """
        if not argss:
            print("** class name missing **")
            return
        else:
            args = argss.split()
            if args[0] not in self.cls_list:
                print("** class doesn't exist **")
                return
            elif args[0] in self.cls_list and len(args) < 2:
                print("** instance id missing **")
                return
            else:
                object_store = models.storage.all()
                key = args[0]+"."+args[1]
                if key in object_store.keys():
                    obj = object_store[key]
                    if len(args) < 3:
                        print("** attribute name missing **")
                        return
                    elif len(args) < 4:
                        print("** value missing **")
                        return
                    else:
                        if obj:
                            if args[3][0] == "\"" or args[3][0] == "\'":
                                args[3] = args[3][1:-1]
                            if args[3].isdigit():
                                args[3] = int(args[3])
                            else:
                                if isfloat(args[3]):
                                    args[3] = float(args[3])
                            setattr(obj, args[2], args[3])
                            # obj.save()
                            models.storage.save()
                else:
                    print("** no instance found **")
                    return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
