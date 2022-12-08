import os
import re

os.chdir(os.path.join(os.environ['HOME'], '2022_adventofcode/day_05'))

#Part 1
with open('input', 'r') as f:
    data = f.readlines()

#Separacion de informacion de cajas e instrucciones
boxes = data[:data.index('\n')-1]
boxes.reverse()
columns = data[data.index('\n')-1].split()
instructions = data[data.index('\n')+1:]

#Extraccion del estado inicial de las cajas
box = {int(x): [] for x in columns}

for line in boxes:
    c = 1
    for i in range(0, len(line), 4):
        if not re.match(r'^\s+$', line[i:i+4]):
            item = line[i:i+4]
            item = re.search(r'\[(.)\]', item).group(1)
            box[c].append(item)
            c += 1
        else:
            c += 1

# Ejecucuion de reglas de movimiento
for l in instructions:
    regex_inst = re.match('move (\d+) from (\d+) to (\d+)', l)
    n_move, n_from, n_to = int(regex_inst.group(1)), int(regex_inst.group(2)), int(regex_inst.group(3))
    for i in range(n_move):
        box[n_to].append(box[n_from].pop(-1))

#Cajas en top
top_boxes = ''.join(x[-1] for x in box.values())

print(f'Cajas al final de la pila: {top_boxes}')

#Part 2
with open('input', 'r') as f:
    data = f.readlines()

#Separacion de informacion de cajas e instrucciones
boxes = data[:data.index('\n')-1]
boxes.reverse()
columns = data[data.index('\n')-1].split()
instructions = data[data.index('\n')+1:]

#Extraccion del estado inicial de las cajas
box = {int(x): [] for x in columns}

for line in boxes:
    c = 1
    for i in range(0, len(line), 4):
        if not re.match(r'^\s+$', line[i:i+4]):
            item = line[i:i+4]
            item = re.search(r'\[(.)\]', item).group(1)
            box[c].append(item)
            c += 1
        else:
            c += 1


# Ejecucuion de reglas de movimiento
for l in instructions:
    regex_inst = re.match('move (\d+) from (\d+) to (\d+)', l)
    n_move, n_from, n_to = int(regex_inst.group(1)), int(regex_inst.group(2)), int(regex_inst.group(3))
    temp_list = []
    for i in range(n_move):
        temp_list.append(box[n_from].pop(-1))
    temp_list.reverse()
    box[n_to] += temp_list

#Cajas en top
top_boxes = ''.join(x[-1] for x in box.values())

print(f'Cajas al final de la pila con CrateMover 9001: {top_boxes}')