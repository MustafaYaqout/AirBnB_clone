#!/usr/bin/python3
import cmd
import json

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt ='(hbnb) '
    classes = {BaseModel}
    

    def do_quit(self, arg):
        """EOF command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass
    
    def do_create(self, arg):
        
        if not arg:
             print("** calss name missing **")
        elif arg not in self.classes:
             print("** class doesn't exist **")
        else:
            new = eval(arg)
            new.save()
            print(new.id)
    
    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not arg:
            print("** class name missing **")   
        elif arg.split() not in self.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2 :
            print("** instance id missing **")
        else:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")   
        elif arg.split() not in self.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2 :
            print("** instance id missing **")
        else:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
        
    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        if not arg:
            print([str(value) for key, value in storage.all().items()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
            
        
         



if __name__ == '__main__':
    HBNBCommand().cmdloop()