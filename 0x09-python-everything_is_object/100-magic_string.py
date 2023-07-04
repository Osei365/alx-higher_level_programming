#!/usr/bin/python3
def magic_string():
    magic_string.attr = getattr(magic_string, 'attr', 0) + 1
    return (("BestSchool, " * (magic_string.attr - 1) + "BestSchool"))
