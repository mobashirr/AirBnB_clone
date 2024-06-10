#!/usr/bin/env python3

'''console module'''


import cmd,sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Simple command interpreter example."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg == "BaseModel":
            new = BaseModel()

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        obj_dict = storage.all()
        args = arg.split()
        if len(args) == 0:
            print([str(obj_dict[key]) for key in obj_dict])
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        print([str(obj_dict[key]) for key in obj_dict if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        instance = obj_dict[key]
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(instance, attr_name):
            try:
                attr_value = eval(attr_value)
            except:
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")

    def emptyline(self):
        """Called when an empty line is entered."""
        pass    # should override this method

    def cmdloop(self, intro=None):
        """Override cmdloop to support non-interactive mode"""
        if not sys.stdin.isatty():
            # Non-interactive mode
            self.stdin = sys.stdin
            self.use_rawinput = False
            while True:
                try:
                    line = self.stdin.readline()
                    if not line:
                        break
                    line = line.rstrip('\r\n')
                    self.onecmd(line)
                except EOFError:
                    break
        else:
            # Interactive mode
            super().cmdloop(intro)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
