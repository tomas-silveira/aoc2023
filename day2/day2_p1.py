from enum import Enum

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

def validate_game(parsed_game):
    for rgb in parsed_game:    
        if rgb[0] > MAX_RED or rgb[1] > MAX_GREEN or rgb[2] > MAX_BLUE:
            return False
    return True 

def main(data):
    total = 0
    for i, game in enumerate(data):
        parsed_game = parse_game(game)
        if validate_game(parsed_game):
            total += i+1
    
    print(total)
    
    

if __name__ == "__main__":
    with open('./input_p1.txt', 'r') as file:
        data = file.readlines()
        main(data)