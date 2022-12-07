import os

os.chdir(os.path.join(os.environ['HOME'], '2022_adventofcode/day_04'))

#Part 1
with open('input', 'r') as f:
    n_subelements = 0
    for l in f.readlines():
        elf_1, elf_2 = l.strip().split(',')
        range_1, range_2 = elf_1.split('-'), elf_2.split('-')
        section_1 = set(range(int(range_1[0]), int(range_1[1])+1))
        section_2 = set(range(int(range_2[0]), int(range_2[1])+1))
        if section_1.issubset(section_2) or section_2.issubset(section_1):
            n_subelements += 1

print(f'Numero de subelementos {n_subelements}')

#Part 1
with open('input', 'r') as f:
    n_subelements = 0
    for l in f.readlines():
        elf_1, elf_2 = l.strip().split(',')
        range_1, range_2 = elf_1.split('-'), elf_2.split('-')
        section_1 = set(range(int(range_1[0]), int(range_1[1])+1))
        section_2 = set(range(int(range_2[0]), int(range_2[1])+1))
        if section_1.intersection(section_2):
            n_subelements += 1

print(f'Numero de elemento solapados {n_subelements}')