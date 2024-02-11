import cmd
import os
import ast
import importlib.util

class MyShell(cmd.Cmd):
    intro = '===============\n Welcome! Simple-pyper can be your personal toolbox to run any pipeline! input help to get start.\n'
    prompt = '(myshell) '

    def do_run(self, arg):
        'Run a Python file with arguments:  RUN [filename] [arg1] [arg2] ...'
        args = arg.split()
        if not args:
            print("Please provide a filename.")
        elif not os.path.isfile(args[0]):
            print(f"{args[0]} does not exist.")
        else:
            with open(args[0]) as file:
                tree = ast.parse(file.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == 'main':
                    required_args = [arg.arg for arg in node.args.args]
                    if len(args[1:]) != len(required_args):
                        print(f"Invalid number of arguments. Expected: {required_args}")
                        return
            spec = importlib.util.spec_from_file_location("module.name", args[0])
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.main(*args[1:])

    def help_run(self):
        print("\n".join([
            "run [filename] [arg1] [arg2] ...",
            "Run a Python file with arguments.",
            ""
        ]))

    def do_exit(self, arg):
        'Exit the shell:  EXIT'
        print("Goodbye!")
        return True

    def help_exit(self):
        print("\n".join([
            "exit",
            "Exit the shell.",
            ""
        ]))

if __name__ == '__main__':
    MyShell().cmdloop()