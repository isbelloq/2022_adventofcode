import os

os.chdir(os.path.join(os.environ['HOME'], '2022_adventofcode/day_01'))

elf_calorie = [0]
elf_index = 0

#Extraccion de calorias por elfo
with open('input', 'r') as f:
    for l in f.readlines():
        if l != '\n':
            elf_calorie[elf_index] += float(l)
        elif l == '\n':
            elf_index += 1
            elf_calorie.append(0)

#Encontrar al elfo con mayor cantidad de calorias
max_calories = max(elf_calorie)
max_elf_index = elf_calorie.index(max_calories)

print(f'Elf: {max_elf_index}\nCalories: {max_calories}')

# Part 2
#Top n elfos con mas comida
top_n = 3
top_calories = 0
for top_elf in range(top_n):
    top_calories += max(elf_calorie)
    elf_calorie.remove(max(elf_calorie))

print(f'\nTop {top_n} Elves: {top_calories}')