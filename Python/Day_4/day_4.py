import re

print("Advent Of Code - Day 4")

PUZZLEINPUT = "284639-748759"
lower_bound,upper_bound = PUZZLEINPUT.split('-')
valid_passwords = 0
valid_passwords_2 = 0

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
    
    if rule1 and rule2:
        valid_passwords += 1

print(f'Part 1: {valid_passwords}')

# def same_digits_group(password):
#     matchs = re.match(r"(.)\1",pw)
#     if match:
#         if (len(match.group())) is 2:
#             return True
#         else:
#             return False    
#     else:
#         return False

# def same_digits_group(password):
#     matches = re.findall(r"(([0-9])\2)",password)    
#     for match in matches:
#         print(f'match is {match} and length is {len(matches[0])} for pw {pw}')
#         if len(matches[0]) == 2:
#             return True
#         else:
#             return False

def same_digits_group(password):
    password = list(password)

    for i in range(0,5):
        if password[i] == password[i+1] and (i == 0 or password[i] != password[i-1]) and  (i == 4 or password[i] != password[i+2]):
            return True
    return False

for i in range(int(lower_bound),int(upper_bound)):
    rule1 = same_digits_group(str(i))
    rule2 = decreasing_digit(str(i))
    
    if rule1 and rule2:
        valid_passwords_2 += 1

print(f'Part 2: {valid_passwords_2}')


