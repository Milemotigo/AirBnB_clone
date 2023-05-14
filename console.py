#!/usr/bin/python3

'''
    a program called console.py that contains the entry point of the command interpreter
'''
import cmd
from models.base_model import BaseModel

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
            if len(argss) > 0:
                args = argss.split()
            if len(args) != 1:
                print("** class doesn't exist **")
            elif len(args) == 1 and args[0] != 'BaseModel':
                print("** class doesn't exist **")
            else:
                inst = BaseModel()
                inst.save()
                print(inst.id)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
