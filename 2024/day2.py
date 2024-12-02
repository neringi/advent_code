# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2024/input_day2.txt','r')

test = [ ['7', '6', '4', '2', '1'],
        ['1', '2', '7', '8', '9'],
        ['9', '7', '6', '2', '1'],
        ['1', '3', '2', '4', '5'],
        ['8', '6', '4', '4', '1'],
        ['1', '3', '6', '7', '9'] ]


with open('input_day2.txt') as content:
    safe = 0
    for line in content:
        report = line.split()
        asc = False
        desc = False
        diffbool = True
        for j in range(1, len(report)):
            diff = abs(int(report[j]) - int(report[j-1]))
            # print(diff)
            if (diff < 1 or diff > 3):
                # print('diff')
                diffbool = False
            if (int(report[j]) - int(report[j-1]) > 0):
                asc = True
            if (int(report[j]) - int(report[j-1]) < 0):
                desc = True
            
            # if asc and desc:
                # print('asc and desc')
        # print(report, asc, desc, diffbool)
        if (not (asc and desc)) and diffbool:
            safe += 1
        
    print('Part1: ', safe)

