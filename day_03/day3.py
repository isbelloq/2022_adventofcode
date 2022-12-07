from functools import reduce
import os

os.chdir(os.path.join(os.environ['HOME'], '2022_adventofcode/day_03'))

points = {chr(x+97): x+1 for x in range(26)}
points.update({chr(x+65): x+27 for x in range(26)})

#Part 1

with open('input', 'r') as f:
    total_points = 0
    for l in f.readlines():
        rucksack =l.strip()
        first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        mixed_elements = set(first).intersection(set(second))
        total_points += sum(points[x] for x in mixed_elements)

print(f'Suma total de puntos: {total_points}')

#Part 2
with open('input', 'r') as f:
    rucksack =[line.strip() for line in f]

total_points = 0
for i in range(0, len(rucksack), 3):
    elements = reduce(lambda x,y: set(x).intersection(set(y)), rucksack[i:i+3])
    total_points += sum(points[x] for x in elements)

print(f'Suma total por equipos de puntos: {total_points}')