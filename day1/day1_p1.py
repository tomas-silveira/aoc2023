import re

with open("./input_p1.txt", "r") as file:
    data = file.readlines()

total = 0
for raw_entry in data:
    nums = re.findall(r'[1-9]', raw_entry.strip())
    calibration_value = nums[0]+nums[-1]
    total += int(calibration_value)
    
print(total)
    
