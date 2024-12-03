import re

# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2024/input_day3.txt','r')

# test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

pattern = r"mul\(\d+,\d+\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Initialize flags
do_enabled = True
# dont_enabled = False

# Find all occurrences of "do()", "don't()", and "mul(x,y)"
matches = re.finditer(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", test)

results = []
for match in matches:
    print(f"Match: {match.group()}")
    if match.group() == "do()":
        do_enabled = True
        print('do')
    elif match.group() == "don't()":
        do_enabled = False
        'do not'
    elif match.group().startswith('mul(') and do_enabled:
        print('mul?', do_enabled)
        num1, num2 = map(int, re.findall(r"\d+", match.group()))
        product = num1 * num2
        results.append(product)


print(results)
print(sum(results))

# Part 1
with open('input_day3.txt') as content:
    results = []
    for line in content:
        i = line.strip().split()
        # print(i)
        matches = re.findall(pattern, line)

        for match in matches:
            # print(match)
            numbers = match[4:-1] 
            # print(numbers)
            num1, num2 = map(int, numbers.split(','))
            product = num1 * num2
            results.append(product)

    print("Part 1 Sum:", sum(results))


# # Part 2

with open('input_day3.txt') as content:
    results = []
    do_enabled = True

    for line in content:
        i = line.strip()
        # print('line', i)
        matches = re.finditer(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", i)

        # print(i)
        for match in matches:
            # print(f"Match: {match.group()}")
            if match.group() == "do()":
                do_enabled = True
                # print('do')
            elif match.group() == "don't()":
                do_enabled = False
                # 'do not'
            elif match.group().startswith('mul(') and do_enabled:
                # print('mul?', do_enabled)
                num1, num2 = map(int, re.findall(r"\d+", match.group()))
                product = num1 * num2
                results.append(product)


        # print(results)
        # print(sum(results))


    print("Part 2 Sum:", sum(results))
