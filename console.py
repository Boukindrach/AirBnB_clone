#!/usr/bin/python3
"""Defines the HBnB console."""


import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB."""

    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
        }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Override the default behavior
        to do nothing on an empty input line.
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        print(new_instance.id)
        storage.save()

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on class name and id.
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance = storage.all().get(f"{args[0]}.{args[1]}")
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if not Storage.get(args[0], args[1]):
            print("** no instance found **")
            return
        Storage.delete(args[0], args[1])

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name.
        """

        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        print([str(instance) for instance in instances.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute.
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance = storage.all().get(f"{args[0]}.{args[1]}")
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
