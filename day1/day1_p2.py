from typing import List

DIGITS = {"one": '1', 
          "two": '2', 
          "three": '3', 
          "four": '4', 
          "five": '5',
          "six": '6',
          "seven": '7', 
          "eight": '8', 
          "nine": '9'}


def decode(code: str):
    result = []
    for i, first_char in enumerate(code):
        if first_char.isnumeric():
            result.append(first_char)
            continue
    
        curr_word = first_char
        for next_char in code[i+1:]:
            curr_word += next_char
            if curr_word in DIGITS.keys():
                result.append(DIGITS[curr_word])
                break
           
    return result

# TEST
assert decode('two1nine') == ['2', '1', '9']
assert decode('eightwothree') == ['8', '2', '3']
assert decode('abcone2threexyz') == ['1', '2', '3']
assert decode('xtwone3four') == ['2', '1', '3', '4']
assert decode('4nineeightseven2') == ['4', '9', '8', '7', '2']
assert decode('zoneight234') == ['1', '8', '2', '3', '4']
assert decode('jdiseveninekdo') == ['7', '9']


def main(entries: List[str]) -> int:
    total = 0
    for raw_entry in entries:
        decoded_entry = decode(raw_entry.strip())
        calibration_value = int(decoded_entry[0]+decoded_entry[-1])
        total += calibration_value
    return total
        
           
# ===================== SOLVE =======================
with open("./input_p2.txt", "r") as file:
    data = file.readlines()
    
result = main(data)
print(result)
