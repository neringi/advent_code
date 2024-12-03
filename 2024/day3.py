import re

# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2024/input_day3.txt','r')

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

pattern = r"mul\(\d+,\d+\)"

matches = re.findall(pattern, test)

results = []
for match in matches:
    # print(match)
    numbers = match[4:-1] 
    print(numbers)
    num1, num2 = map(int, numbers.split(','))
    product = num1 * num2
    results.append(product)

print(results)



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


# Part 2

