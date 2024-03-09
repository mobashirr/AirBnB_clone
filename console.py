import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    def preloop(self):
        # self.prompt = "(hbnb) "
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF help quit\n")

    def do_quit(self, arg):
        return True  # Returning True will exit the command loop

    def do_EOF(self, arg):
        pass

    def help_EOF(self):
        print("EOF command to exit the program")

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass

def interactive_mode():
    HBNBCommand.prompt = "(hbnb) "
    HBNBCommand().cmdloop()

def noninteractive_mode():
    HBNBCommand.prompt = "$ "
    print("Running in non-interactive mode")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

