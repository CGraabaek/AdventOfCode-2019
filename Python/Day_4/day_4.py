import re

print("Advent Of Code - Day 4")

PUZZLEINPUT = "284639-748759"
lower_bound,upper_bound = PUZZLEINPUT.split('-')
valid_passwords = 0

def same_digits(password):
    if re.search(r"(.)\1", password):
        return True
    else:
        return False

def decreasing_digit(password):
    password = list(str(password))
    if password == sorted(password):
        return True
    return False

for i in range(int(lower_bound),int(upper_bound)):
    rule1 = same_digits(str(i))
    rule2 = decreasing_digit(str(i))
    
    if(rule1 and rule2):
        valid_passwords += 1

print(f'Part 1: {valid_passwords}')