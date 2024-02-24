import re
import sys
pattern = re.compile(r'on|off|=|[+\-]?\d+', re.IGNORECASE)


def find_items(l):
    return [m.group() for m in pattern.finditer(l)]


total = 0
active = True
for line in sys.stdin:
    for item in find_items(line):
        if item == 'on':
            active = True
        elif item == 'off':
            active = False
        elif item == '=':
            print(total)
        elif active:
            total += int(item)
