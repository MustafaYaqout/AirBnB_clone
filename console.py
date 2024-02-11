#!/usr/bin/python3

import cmd
import argparse
from models import storage

class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
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
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if not arg:
            print([str(value) for key, value in storage.all().items()])
        elif arg not in self.classes:
            print("** class doesn't exist **")


def non_interactive_mode(args):
    if args.command == "create":
        if not args.arguments:
            print("** class name missing **")
        elif args.arguments[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = eval(args.arguments[0])()
            new.save()
            print(new.id)
    elif args.command == "show":
        # Handle show command here, similar to existing logic
        pass
    elif args.command == "destroy":
        # Handle destroy command here, similar to existing logic
        pass
    elif args.command == "all":
        # Handle all command here, similar to existing logic
        pass
    # Add more conditions for other commands as needed

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HBnB Console')
    parser.add_argument('--non-interactive', action='store_true', help='Run in non-interactive mode')
    parser.add_argument('command', nargs='?', default='', help='Command to execute in non-interactive mode')
    parser.add_argument('arguments', nargs='*', help='Arguments for the command in non-interactive mode')
    args = parser.parse_args()

    if args.non_interactive:
        non_interactive_mode(args)
    else:
        HBNBCommand().cmdloop()