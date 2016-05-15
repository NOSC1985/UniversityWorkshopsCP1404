"""
Class: ProgrammingLanguage
Author: Nicholas Stanton-Cook
Program Set: Week eight Workshop Tasks
This Class will generate a new variable type "Programming Language" which will determine what properties
a given programming language has including the following.

-Typing
-Reflection
-Year

And will initially store data on these properties for the following languages

-Java
-C++
-Python
-Visual Basic
-Ruby

This Class also includes a __str__ method for print formatting.

"""
__Author__ = "Nicholas Stanton-Cook"


class ProgrammingLanguage:

    def __init__(self, language_name, language_typing, language_reflection, language_year_published):
        """
        Define the base parameters
        :param language_name:
        :param language_typing:
        :param language_reflection:
        :param language_year_published:
        """

        self.name = language_name
        self.typing = language_typing
        self.reflection = language_reflection
        self.published = language_year_published

    def is_dynamic(self):
        """
        Check the self.typing attribute

        if self.typing
        :return: dynamic_check
        """

        if self.typing == "Dynamic":
            dynamic_check = True
        else:
            dynamic_check = False

        return dynamic_check

    def __str__(self):

        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.published)