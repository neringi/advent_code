# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2025/input_day3.txt','r')

test = ['987654321111111', '811111111111119', '234234234234278','818181911112111']

with open('input_day3.txt') as content:
    content = "\n".join(content.readlines())
    content = content.strip()
    content= content.split('\n')
    jolts = []
    for bank in content:
        digits = [int(x) for x in list(bank)]
        print(digits)

        first = 1
        second = 1
        jolt = first*10 + second

        for i, outer in enumerate(digits[:-1]):
            if first<outer and (outer*10+second)>jolt:
                first = outer
                second = 1
                jolt = first*10 + second
                print('first updated ', first, 'jolt: ', jolt)

            for inner in digits[i+1:]:
                print(outer, inner)

                if (first*10+inner)>jolt:
                    second = inner
                    jolt = first*10+second
                    print('second updated ', second, 'jolt: ', jolt)

        print(first, second, jolt)
        jolts.append(jolt)
    print(jolts)
    print(sum(jolts))
