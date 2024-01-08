
# simplified interpreter that works for hello.py

import os
import sys
import re

if len(sys.argv) < 2:
    print("You must supply an input.")
    quit()

variables = {}
current_char = 0
source = ""

with open(sys.argv[1]) as file:
    source = file.read()

def squeeze():
    global current_char
    while current_char < len(source) and source[current_char] in [" ","\t","\n"]:
        current_char += 1


def handle_comment():
    global current_char
    while source[current_char] != "\n" and current_char < len(source):
        current_char += 1
    current_char += 1


def handle_assignment():
    global current_char
    var_name = re.findall(r"^([a-zA-Z0-9]+)\s+?=", source[current_char:])[0]
    
    current_char += len(var_name)
    squeeze()
    current_char += 1
    squeeze()

    var_content = ""
    if source[current_char] == "\"":
        current_char += 1
        while source[current_char] != "\"":
            var_content += source[current_char]
            current_char += 1

        current_char += 1
        variables[var_name] = var_content
    
    if source[current_char] in [str(x) for x in range(10)]:
        while source[current_char] != "\n":
            var_content += source[current_char]
            current_char += 1
        variables[var_name] = var_content
    squeeze()


def handle_print():
    global current_char
    current_char += 5
    squeeze()
    current_char += 1

    var_name = ""
    while source[current_char] != ")":
        var_name += source[current_char]
        current_char += 1
    current_char += 1
    squeeze()

    try:
        print(variables[var_name])
    except:
        print("unknown variable name: {}".format(var_name))
        quit()


while current_char < len(source):

    if source[current_char:].startswith("#"):
        handle_comment()
        continue

    if re.match(r"^([a-zA-Z0-9]+)\s+?=", source[current_char:]):
        handle_assignment()
        continue

    if re.match(r"^print\s*\(", source[current_char:]):
        handle_print()
        continue

    current_char += 1
