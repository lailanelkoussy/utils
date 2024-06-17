import argparse
import sys


# To run this
# python executing_specific_function_based_on_cmd_param.py create param

def create(param_1):
    print('Executing create')


def add(param_1):
    print('Executing add')

def main():
    parser = argparse.ArgumentParser(description="Run functions from run_python module")
    parser.add_argument("function_name", choices=["create", "add"], help="Name of the function to execute")
    parser.add_argument("params", nargs="*", help="Parameters to pass to the function")
    args = parser.parse_args()

    func = getattr(sys.modules[__name__], args.function_name)

    func(args.params)


if __name__ == "__main__":
    main()
