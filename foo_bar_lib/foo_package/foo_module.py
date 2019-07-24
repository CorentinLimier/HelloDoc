"""
foo module
"""

class FooClass():
    """This is FooClass
    
    It is not very useful, it serves as an example

    Attributes:
        foo_attr (str): Any string that makes you feel happy
    """

    def __init__(self, foo_param):
        """This is the constructor

        And here I explain quite nothing about this method

        :param foo_param: string that is stored in foo_attr
        :type foo_param: str
        :rtype: None
        """
        self.foo_attr = foo_param

    def foo(self):
        """This is foo
 
        It is very powerful. Be cautious when using it.
        With great power comes great responsability

        :returns: foo_attr
        :rtype: str
        """    
        return self.foo_attr
