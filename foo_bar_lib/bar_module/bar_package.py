"""
bar package
"""

class BarClass():
    """This is BarClass
    
    It is not very useful, it serves as an example

    Attributes:
        bar_attr (str): Any string that makes you feel happy
    """

    def __init__(self, bar_param):
        """This is the constructor

        And here I explain quite nothing about this method

        :param bar_param: string that is stored in bar_attr
        :type bar_param: str
        :rtype: None
        """
        self.bar_attr = bar_param

    def bar(self):
        """This is bar
 
        It is very powerful. Be cautious when using it.
        With great power comes great responsability

        :returns: bar_attr
        :rtype: str
        """    
        return self.bar_attr
