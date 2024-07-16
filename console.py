#!/usr/bin/env python3

'''console module'''


import cmd,sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "Review": Review,
    "City": City,
    "Amenity": Amenity,
    "Place": Place
}

class HBNBCommand(cmd.Cmd):
    """Simple command interpreter example using the HBNBcommand module:"""

    prompt = '(hbnb) '

    def preloop(self):
        '''
        this method run when the console start
        ensure restoring the data from database file
        '''
        storage.reload()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Create a new instance of choosen class, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        elif arg in classes:
            # if the class name is valid:
            new = classes[arg]() # create instance of that calss
            storage.new(new)    # save the new instance in storage class
            storage.save()      # save it to the database file
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] in classes:
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                all_users = storage.all()
                key = "{}.{}".format(args[0], args[1])

                for user,object in all_users.items():
                    if key == user:
                        print(f"{object}")
                        return
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")
            return

    def do_destroy(self, arg):
        '''destroy an instance of a class'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] in classes:
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                all_users = storage.all()
                key = "{}.{}".format(args[0], args[1])

                for user,object in all_users.items():
                    if key == user:
                        del all_users[key] # delete the user from the storage class
                        storage.save()     # apply the changes to the database file
                        return
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")
            return
        
    def do_all(self, arg):
        """Prints all string representation of all instances."""
        obj_dict = storage.all()
        args = arg.split()
        if len(args) == 0:
            print([str(obj_dict[key]) for key in obj_dict])
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        print([str(obj_dict[key]) for key in obj_dict if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1] # get the key format to get the user from the storage var
        obj_dict = storage.all() # get all user

        if key not in obj_dict:
            ''' if the instance is not in the database:'''
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
        if True:
            try:
                attr_value = eval(attr_value)
            except:
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")

    def do_EOF(self, arg):
        """Handle the EOF signal to exit the console"""
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass    # i override this method so that it won't do anything

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