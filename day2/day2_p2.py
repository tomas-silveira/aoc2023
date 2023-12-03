from enum import Enum
import numpy as np

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

class CubeColours(Enum):
    red = 0
    green = 1
    blue = 2       
    
def parse_subset(subset: str):
    cubes = subset.split(', ')
    rgb = [0, 0, 0]
    for cube in cubes:
        value, colour = cube.split(' ')
        ix = CubeColours[colour].value
        rgb[ix] = int(value)
    
    return rgb

assert parse_subset('7 blue, 9 red, 1 green') == [9, 1, 7]
assert parse_subset('8 green') == [0, 8, 0]
assert parse_subset('5 red, 1 green') == [5, 1, 0]


def parse_game(line: str) -> bool:
    _, game_raw = line.strip().split(': ')
    subsets = game_raw.split("; ")
    rgb = [parse_subset(subset) for subset in subsets]    
    return rgb


def main(data):
    total = 0
    for game in data:
        parsed_game = parse_game(game)
        game_matrix = np.array(parsed_game)
        r, g, b = game_matrix.max(axis=0)
        total += r*g*b
        
    print(total)
        
    
    
if __name__ == "__main__":
    with open('./input_p1.txt', 'r') as file:
        data = file.readlines()
        main(data)