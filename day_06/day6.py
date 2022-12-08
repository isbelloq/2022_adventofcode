import os

os.chdir(os.path.join(os.environ['HOME'], '2022_adventofcode/day_06'))

#Part 1
with open('input', 'r') as f:
    buffer = f.readlines()[0]
    buffer = buffer.strip()

def num_char_processing(buffer: str, min_char: int = 4) -> int:
    '''
    Funcion de extraccion de longitud de procesamiento de Buffer

    Parameters
    ----------
    buffer: str
        Cadena de caracter a procesar
    min_char: int = 4
        Numero de caracteres en la comparacion
    Returns
    -------
    int
        Numero de caracteres para ser procesados
    '''
    for i in range(len(buffer)):
        if len(set(buffer[i:i+min_char])) == min_char:
            break
    return i+min_char
    
# Ejemplos
# print(num_char_processing('mjqjpqmgbljsphdztnvjfqwrcgsmlb'))
# print(num_char_processing('bvwbjplbgvbhsrlpgdmjqwftvncz'))
# print(num_char_processing('nppdvjthqldpwncqszvftbrmjlhg'))
# print(num_char_processing('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'))
# print(num_char_processing('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))
print(f'Numero de caracteres para ser procesados: {num_char_processing(buffer)}')

# Parte 2
# print(num_char_processing('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14))
# print(num_char_processing('bvwbjplbgvbhsrlpgdmjqwftvncz', 14))
# print(num_char_processing('nppdvjthqldpwncqszvftbrmjlhg', 14))
# print(num_char_processing('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14))
# print(num_char_processing('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14))
print(f'Numero de caracteres para ser procesados: {num_char_processing(buffer, 14)}')