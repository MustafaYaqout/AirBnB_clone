#!/usr/bin/python3
"""Console module"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""

    prompt = "(hbnb) "
    classes = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothint line"""
        pass
    

            
if __name__ == '__main__':
    HBNBCommand().cmdloop()