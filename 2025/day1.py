# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2025/input_day1.txt','r')

test = ['L68',
'L30',
'R48',
'L505',
'R60',
'L55',
'L1',
'L99',
'R14',
'L82']

with open('input_day1.txt') as content:
    dial = 50
    count=0
    for turn in file:
        if turn[0]== 'L' :
            dial = dial - int(turn[1:])%100
            if dial < 0 : 
                dial = dial + 100
        elif turn[0] == 'R' :
            dial = dial + int(turn[1:])%100
            if dial >= 100 : 
                dial = dial -100
        if dial == 0:
            count+=1
        # print(turn, 'dial is now', dial)
    print('Number:',count)


# Part 2
# with open('input_day1.txt') as content:
#     dial = 50
#     count=0

#     print('********** starting the rotations *************')

#     for turn in test:
#         dist=int(turn[1:])
#         clicks=0
#         # print('***TURN:', content)
#         if turn[0]== 'L' :
#             dial = dial - dist%100
#             clicks= (dist - dist%100) / 100
#             if dial < 0 : 
#                 dial = dial + 100
#                 count+=1
#         elif turn[0] == 'R' :
#             dial = dial + dist%100
#             clicks = (dist - dist%100) / 100
#             if dial >= 100 : 
#                 dial = dial-100
#                 if dial == 0 :
#                     count -=1
#         if dial == 0:
#             count+=1
#             # print('count is now: ',count)
       
#         count+=clicks
#         print('***TURN ', turn, '***')
#         print('Dial: ', dial,' clicks: ', clicks, ' Count:', count)
#     print('Part2: total count:',count)
