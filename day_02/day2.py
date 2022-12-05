import os

os.chdir(os.path.join(os.environ['HOME'], '2022_adventofcode/day_02'))

#Parte 1
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

points = 0
#Extraccion de puntaje
with open('input', 'r') as f:
    for l in f.readlines():
        opponent, me =l.strip().split(' ')
        points += rules_dict[me]['points'] + rules_dict[me][opponent]

print(f'Puntos totales: {points}')

#Parte 2

new_rules_dict = {
    #Lose
    'X': {
        'points': 0,
        'A': 3,
        'B': 1,
        'C': 2
    },
    #Draw
    'Y':{
        'points': 3,
        'A': 1,
        'B': 2,
        'C': 3
    }, 
    #Win
    'Z':{
        'points': 6,
        'A': 2,
        'B': 3,
        'C': 1
    }
}

points = 0
#Extraccion de puntaje nuevas reglas
with open('input', 'r') as f:
    for l in f.readlines():
        opponent, me =l.strip().split(' ')
        points += new_rules_dict[me]['points'] + new_rules_dict[me][opponent]

print(f'Puntos totales nuevas reglas: {points}')