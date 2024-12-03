# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2024/input_day2.txt','r')

test = [ ['7', '6', '4', '2', '1'],
        ['1', '2', '7', '8', '9'],
        ['9', '7', '6', '2', '1'],
        ['1', '3', '2', '4', '5'],
        ['8', '6', '4', '4', '1'],
        ['1', '3', '6', '7', '9'] ]

def checkSafeReport(report):
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
        return 1
    else: 
        return 0
    
with open('input_day2.txt') as content:
    safe = 0
    for line in content:
        report = line.strip().split()

        if checkSafeReport(report) == 1:
            safe += 1
        
    print('Part1: ', safe)

# PART 2

print("PART 2")

with open('input_day2.txt') as content:
    safeReportCount = 0
    for line in content:
        report = line.strip().split()

        if checkSafeReport(report) == 1:
            safeReportCount += 1
        else:
            for i, level in enumerate(report):
                # print("DEBUG: Report is:", report)

                copy = report.copy()
                copy.pop(i)
                if checkSafeReport(copy) == 1:
                    safeReportCount += 1
                    break
    print("Part 2 Safe Report Count: ", safeReportCount)

