#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt ='(hbnb) '
    

    def do_quit(self, *args):
        """EOF command to exit the program"""
        return True
    
    def do_EOF(sel, *args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()