#!/usr/bin/python3
'''
shopper command line interface module
'''

import cmd
from models.base_model import BaseModel
import models


class ShopperCommand(cmd.Cmd):
    '''
    A program called console.py that contains the entry point of
    the command interpreter:
    '''
    prompt = "(scmd) "

    def do_quit(self, arg):
        '''
        quits the program
        '''
        return True

    def do_EOF(self, arg):
        '''
        Quits the program
        '''
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        '''
        Creates a new instance of BseModel
        '''
        if args == "":
            print("** class name missing **")
            return
        elif args != globals()[args].__name__:
            print("** class doesn't exist **")
            return
        model = globals()[args]()
        models.storage.save()
        print(model.id)
        return

if __name__ == "__main__":
    ShopperCommand().cmdloop()
