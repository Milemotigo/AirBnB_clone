#!/usr/bin/python3

'''
    a program called console.py that contains the entry point of the command interpreter
'''
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
        prompt = '(hbnb)    '

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
                elif len(args) == 1 and args[0] != 'BaseModel':
                    print("** class doesn't exist **")
                    return
                else:
                    inst = BaseModel()
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
                    #print("fail")
                    return
                else:
                    if len(args) == 1 and args[0] != "BaseModel":
                        print("** class doesn't exist **")
                        return
                    if len(args) == 1 and args[0] == "BaseModel":
                        print("** instance id missing **")
                        return
                    if len(args) == 2 and args[0] == "BaseModel":
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
                    #print("fail")
                    return
                else:
                    if len(args) == 1 and args[0] != "BaseModel":
                        print("** class doesn't exist **")
                        return
                    if len(args) == 1 and args[0] == "BaseModel":
                        print("** instance id missing **")
                        return
                    if len(args) == 2 and args[0] == "BaseModel":
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
                print("not on the class name")
                return
            else:
                args = argss.split()
                if len(args) > 1:
                    #########
                    return
                else:
                    if len(args) == 1 and args[0] != "BaseModel":
                        print("** class doesn't exist **")
                        return
                    else:
                        object_store = models.storage.all()
                        #print(f"[{object_store}]"
                        #print(str(object_store))
                        item_str = []
                        for value in object_store.values():
                            val_str = f"{value}"
                            item_str.append(val_str)

                        result = ", ".join(item_str)
                        print(f"[\"{result}\"]")






if __name__ == '__main__':
    HBNBCommand().cmdloop()
