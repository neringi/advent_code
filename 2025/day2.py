# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2025/input_day2.txt','r')

test = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224',
'1698522-1698528','446443-446449','38593856-38593862','565653-565659',
'824824821-824824827','2121212118-2121212124']

with open('input_day2.txt') as content:
    content = "\n".join(content.readlines())
    content = content.strip()
    content= content.split(',')
    # print(content)
    summed = 0
    for i in content:
        print(i)
        i=i.split('-')
        a=int(i[0])
        b=int(i[1])
        for j in range(a, b+1):
            length = len(str(j))
            left=str(j)[:(round(length/2))]
            right=str(j)[(round(length/2)):]
            if left == right:
                # print(left, j, right)
                summed+=j

    print('PART 1 Total sum: ', summed)

# part 2

with open('input_day2.txt') as content:
    content = "\n".join(content.readlines())
    content = content.strip()
    content= content.split(',')
    arr = []

    for i in test:
        i=i.split('-')
        a=int(i[0])
        b=int(i[1])
        for j in range(a, b+1):
            length = len(str(j))

            print(j, length)