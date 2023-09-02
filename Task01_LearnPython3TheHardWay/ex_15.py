# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/2 9:57
@Author ： keatingnobug
@File ：ex_15.py
"""
from sys import argv

script,filename=argv
txt=open(filename)
print(f"Here's your file {filename}:")
print(txt.read())
print("Type the filename again:")
file_again=input("> ")
txt_again=open(file_again)
print(txt_again.read())