import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command interpreter example."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
