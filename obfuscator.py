import noiser
import os
path = '\\'.join(__file__.split('\\')[:-1]) + '\\'

with open(path+'test.py', 'r') as f:
    lines = f.readlines()

with open(path+'test.py', 'w') as f:
    lines = noiser.noiser(lines, 1, 0)
    f.writelines(lines)

exit()
with open(r'C:\Users\waitman\OneDrive\Documents\codemann\python\obfuscator\test.py', 'r') as f:
    lines = f.readlines()

# TODO make strings and numbers a set of instruccions
# scratch minifier
# exec loops


def append(n, l=[]):
    l.append(n)
    return l


l1 = append(0)
l2 = append(2)
iii
