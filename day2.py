import re

# maximum number of blocks per colour
maxlist = [[12,'red'],[13,'green'],[14,'blue']]


# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code_2023/input_day2.txt','r')

with open('input_day2.txt') as content:
    # reset the sum
    sum = 0
   
    for line in content:
        check = []
        print("****************")
        print(line)
        game_id = line.split(':')[0]
        # print(game_id)
        game_num = re.search(r'\d+',game_id).group()
        print(game_num)
        games = line.split(':')[1].split(';')
        for game in games: 
            for round in game.split(', '):
                [count, color] = round.split()
                # print(count, color)
                for maxno in maxlist:
                    if color == maxno[1] and int(count) <= maxno[0] :
                        # print(f"{count} <= {maxno[0]} for colour {maxno[1]}")
                        # print('pass')
                        check.append(1)
                    elif color == maxno[1] and int(count) > maxno[0] :
                        # print("fail")
                        check.append(0)
        # print(check)
        if 0 not in check:
            print("ok")
            sum = sum + int(game_num)

print(f"The sum is {sum}")

file.close()





    #     breakup = line.split(":")
    #     print(breakup)
    #     breakup2 = breakup.split(";")
    #     print(breakup2)
        # for game in line:
        #     idk = game.split(":")
        #     print(idk)



# test cases all except Game 3 should pass
# test1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
# test2 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
# test3 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
# test4 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
# test5 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

# game_id = test1.split(':')[0]
# games = test1.split(':')[1].split(';')

# for game in games: 
#     for round in game.split(', '):
#         [count, color] = round.split()
#         print(count, color)
#         for maxno in maxlist:
#             if color == maxno[1] and int(count) <= maxno[0] :
#                 print(f"{count} <= {maxno[0]} for colour {maxno[1]}")
#                 print("pass")
#             elif color == maxno[1] and int(count) > maxno[0] :
#                 print("fail")



# put test case in lists
# test1read = [[ [3,',blue'],[4,'red'] ], [[1,'red'],[2,'green'],[6,'blue']], [[2,'green']] ]
# test3read = [[ [8,'green'],[6,'blue'],[20,'red']], [ [5,'blue'],[4,'red'],[13,'green']],[ [5,'green'],[1,'red']]]


# loop through lists to check each value
# for turn in test3read:
#     # print(turn)
#     for item in turn:
#         # print(item)
#         for maxno in maxlist:
#             if item[1] == maxno[1] and item[0] <= maxno[0] :
#                 print(f"{item[0]} <= {maxno[0]} for colour {maxno[1]}")
#                 print("pass")
#             elif item[1] == maxno[1] and item[0] > maxno[0] :
#                 print("fail")
               
