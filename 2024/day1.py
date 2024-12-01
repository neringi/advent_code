# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2024/input_day1.txt','r')


with open('input_day1.txt') as content:
    leftList = []
    rightList = []
    distance = []
    for line in content:
        left, right = line.split()
        leftList.append(left)
        rightList.append(right)

    # print("left :", leftList)
    # print("right: ", rightList)
    leftList.sort()
    rightList.sort()

    distance = [abs(int(x)-int(y)) for x,y in zip(leftList, rightList)]

    print("/n distance: ", distance)

    total_distance = sum(distance)

    print("Part 1 solution /n")
    print("Total Distance: ", total_distance)


# Part 2

with open('input_day1.txt') as content:
    leftList = []
    rightList = []
    distance = []
    for line in content:
        left, right = line.split()
        leftList.append(left)
        rightList.append(right)

    # print("left :", leftList)
    # print("right: ", rightList)
    leftList.sort()
    rightList.sort()

    similarityList = []
    for i in leftList:
        count = 0
        for j in rightList:
            if int(i) == int(j):
                count += 1
        similarity = int(i) * count 
        similarityList.append(similarity)

    total_similarity = sum(similarityList)
    print("Part 2")
    print("Similarity Total: ", total_similarity)
