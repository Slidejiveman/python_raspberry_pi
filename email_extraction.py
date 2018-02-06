import re

""" This program tests the use or regular expressions
    in order to pars out an email from a string """

# This pattern matches one or more word characters, a dot, or
# a dash. Then it is followed by @, followed by the same rules,
# then there is a dot followed by one or more word characters
# or a dot. It finds a single email address. findall() gets more.
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())
