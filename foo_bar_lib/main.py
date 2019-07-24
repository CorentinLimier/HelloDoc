"""
This is main script

Usage: main.py [-h] [-f FOO] [-b BAR]

Optional arguments:
    -h, --help         show this help message and exit

    -f FOO, --foo FOO

    -b BAR, --bar BAR

Examples:
    $ python main.py --foo foo --bar bar
"""
import argparse

import foo_module.foo_package
import bar_module.bar_package


def main(foo_obj, bar_obj):
    """main function

    This function is called when script is executed.

    :param foo_obj: The foo parameter
    :type foo_obj: foo_module.foo_package.FooClass
    :param bar_obj: The bar parameter
    :type bar_obj: foo_module.foo_package.BarClass
    :returns: True for success, False otherwise 
    :rtype: bool
    """

    foo_result = foo_obj.foo()
    bar_result = bar_obj.bar()
    print(foo_result, bar_result)
    return foo_result and bar_result


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--foo", default="foo")
    parser.add_argument("-b", "--bar", default="bar")

    args = parser.parse_args()

    foo_obj = foo_module.foo_package.FooClass(args.foo)
    bar_obj = bar_module.bar_package.BarClass(args.bar)

    main(foo_obj, bar_obj)
