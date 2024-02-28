#!/usr/bin/python3
"""Module console"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User", "State", "City", "Place",
                         "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City", "Place",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City", "Place",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if not arg:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in ["BaseModel", "User", "State", "City", "Place",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items()
                   if args[0] in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City", "Place",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        """Empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
