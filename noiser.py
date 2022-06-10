import random

dependency = ['time', 'random', 'glob', 'math', 'os', 'threading',
              'glob', 'turtle', 'abc', 'sys',  'math']

# gets random noise useless piece of code
path = '\\'.join(__file__.split('\\')[:-1]) + '\\'
with open(path+'test.py', 'r') as f:
    lines = f.readlines()


def noiss():
    randomdepo = random.randint(0, len(dependency)-1)
    randomdepo = dependency[randomdepo]

    noise = {1: 'pass\n',
             2: 'sleep(0)\n', 3: f'import {randomdepo}\n', 4: 'for i in range(8):\n;    pass\n', }

    randomnoise = noise[random.randint(1, len(noise))]

    return randomnoise

# checks how indented a line is


def Indented(string):
    element = ' '
    count = 0

    while element == ' ':
        element = string[count]
        count += 1

    if count != 0:
        count -= 1
    return count

# generates poluted newlines


def noised(lines):
    newlines = []
    count = 0
    for i in range(len(lines)):
        newlines.append(lines[i])

    for index, line in enumerate(lines):

        indent = Indented(line)

        randomus = noiss()

        # inserts the noise into the lines
        if ';' in randomus:
            randomus = randomus.split(';')
            for ranline in randomus:
                newlines.insert(index + count, ' '*indent + ranline)
                count += 1
        else:
            newlines.insert(index + count, ' '*indent + randomus)
            count += 1

    return newlines

# edits the lines and does some post procesing


def noiser(lines, level, after):
    for i in range(level):
        lines = noised(lines)

    for i in range(after):
        randomus = noiss()

        if ';' in randomus:
            randomus = randomus.split(';')
            for ranline in randomus:
                lines.append(ranline)

        else:
            lines.append(randomus)

    for depo in dependency:
        lines.insert(0, f'from {depo} import *\n')
    return lines


for line in noised(lines):
    print(line)
