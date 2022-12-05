import os

os.chdir(os.path.join(os.environ['HOME'], '2022_adventofcode/day_02'))

rules_dict = {
    #Rock
    'X': {
        'points': 1,
        'A': 3,
        'B': 0,
        'C': 6},
    #Paper
    'Y': {
        'points': 2,
        'A': 6,
        'B': 3,
        'C': 0},
    #Scissors
    'Z': {
        'points': 3,
        'A': 0,
        'B': 6,
        'C': 3},
}

#Parte 1
points = 0
#Extraccion de puntaje
with open('input', 'r') as f:
    for l in f.readlines():
        opponent, me =l.strip().split(' ')
        points += rules_dict[me]['points'] + rules_dict[me][opponent]

print(f'Puntos totales: {points}')