from tinyscript import *

__examples__ = ["", "--test"]

if __name__ == '__main__':
    parser.add_argument("--test", action="store_true", help="test argument")
    initialize(add_demo=True)
    logger.success("First example" if not args.test else "Second example")
