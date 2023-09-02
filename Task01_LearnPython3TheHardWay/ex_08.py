# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/2 9:19
@Author ： keatingnobug
@File ：ex_08.py
"""
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
