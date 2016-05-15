"""
Program: languages
Author: Nicholas Stanton-Cook
Program Set: Week eight Workshop Tasks

This program will test the class ProgrammingLanguage and ensure it functions correctly

"""
__Author__ = "Nicholas Stanton-Cook"

from ProgrammingLanguage import *

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(vb)

programming_language_list = [ruby, python, vb]

print("\nThe Dynamically typed languages are\n")
for language in programming_language_list:

    if language.is_dynamic():
        print(language)
