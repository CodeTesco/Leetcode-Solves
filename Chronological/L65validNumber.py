import re

def isNumber(s):
    pattern = re.compile(r"^[+-]?([0-9]*\.[0-9]+|[0-9]+\.?[0-9]*)((e|E)([+-]?[0-9]+))?$")
    result = pattern.match(s)
    if result:
        return True
    else:
        return False

print(isNumber("-1E"))