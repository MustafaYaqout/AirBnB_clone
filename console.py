#!/usr/bin/python3
"""Console module"""
import cmd

from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""

    prompt = "(hbnb) "
    classes = {'BaseModel', 'User'}

    def do_quit(self, arg):
        """Quit command to exit"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothint line"""
        pass
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes :
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)
            
    def do_show(self, arg):
        """show a new instance of BaseModel,
        saves it (to the JSON file) """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.classes :
            print("** class doesn't exist **")
        elif len(arg.split()) < 2 :
            print("** instance id missing **")
        else:
            key = arg.split()[0] + ' ' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
                
    def do_destroy(self, arg):
        """destroy all instance of BaseModel,
        saves it (to the JSON file) """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.classes :
            print("** class doesn't exist **")
        elif len(arg.split()) < 2 :
            print("** instance id missing **")
        else:
            key = arg.split()[0] + ' ' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
                
    def do_all(self, arg):
        """Prints all string representation of all instances
            based or not on the class name"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items()])
            
        
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()