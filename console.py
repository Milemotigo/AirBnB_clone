#!/usr/bin/python3

'''
    a program called console.py that contains the entry point of the command interpreter
'''
import cmd
import readline

class HBNBCommand(cmd.Cmd):
        prompt = '(hbnb)'

        def do_EOF(self, line):
            return True

        def do_quit(self, line):
            return True

        def emptyline(self):
            pass

        def do_help(self, line):
            if line == "quit":
                print ("Quit command to exit the program")
            else:
                super().do_help(line)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
