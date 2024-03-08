import cmd
import sys

class MyCmd(cmd.Cmd):

    def do_help(self, arg):
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF help quit\n")

    def preloop(self):
        # self.prompt = "(hbnb) "
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF help quit\n")

    def do_quit(self, arg):
        return True  # Returning True will exit the command loop

    def do_EOF(self, arg):
        pass


def interactive_mode():
    MyCmd.prompt = "hbnb "
    MyCmd().cmdloop()

def noninteractive_mode():
    MyCmd.prompt = "$ "
    print("Running in non-interactive mode")

if __name__ == '__main__':
    if not sys.stdin.isatty():
        noninteractive_mode()
    else:
        interactive_mode()

