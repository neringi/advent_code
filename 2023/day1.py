# ------ Part One ------

import re

# Function to reverse a string
def reverse_string(string):
    # Returns the reversed string by slicing from the end to the beginning
    return string[::-1]

# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code_2023/input_day1.txt','r')

# Loop through each line to get the digits and the sum
# with open('input_day1.txt') as content:
#     # reset the sum
#     sum = 0
#     for i in content:
#         # print(i)
        
#         # Use regex and re.search to find the first digit
#         matchfirst = re.search(r'\d',i)
#         getfirstdigit = matchfirst.group()
#         # print(getfirstdigit)

#         # Reverse line
#         reverseline = reverse_string(i)
#         # print(reverseline) 

#         # Use regex and re.search to find the last digit
#         matchlast = re.search(r'\d',reverseline)
#         getlastdigit = matchlast.group()
#         print(getlastdigit)

#         # Concatenate the two digits to make a two-digit number
#         twodigits = int(str(getfirstdigit) + str(getlastdigit))
#         print(twodigits)

#         # Add the number to the sum
#         sum = sum + int(twodigits)

# print(f"The sum is {sum}")

# file.close()


# ------ Part Two -------

with open('input.txt') as content:
    sum = 0
    for i in content:
        print(i)
        positions = []
        rpositions = []
        for index, char in enumerate(i):
            
            # Checking if char is numeric
            if char.isdigit():
                # Printing number and its position
                # print('The first number is:', char)
                # print('Index of first number is:', index)
                positions.append(index)
                break
        find1 = i.find("one")
        # print(find1)
        positions.append(find1)

        find2 = i.find("two")
        # print(find2)
        positions.append(find2)

        find3 = i.find("three")
        # print(find3)
        positions.append(find3)

        find4 = i.find("four")
        # print(find4)
        positions.append(find4)

        find5 = i.find("five")
        # print(find5)
        positions.append(find5)

        find6 = i.find("six")
        # print(find6)
        positions.append(find6)

        find7 = i.find("seven")
        # print(find7)
        positions.append(find7)

        find8 = i.find("eight")
        # print(find8)
        positions.append(find8)

        find9 = i.find("nine")
        # print(find9)
        positions.append(find9)

        # print(positions)

        findfirst = positions.index(min([i for i in positions if i >= 0]))
        
        # print(findfirst)

        if findfirst == 0 :
            firstdigit = char
        elif findfirst > 0 :
            firstdigit = findfirst
        
        print(firstdigit)

        reversed = reverse_string(i)

        for index2, char2 in enumerate(reversed):
            
            # Checking if char is numeric
            if char2.isdigit():
                # Printing number and its position
                # print('The last number is:', char2)
                lastindex = len(reversed.strip()) - index2
                # print('Index of last number is:', lastindex)
                rpositions.append(lastindex)
                break
        
        rfind1 = i.rfind("one")
        # print(rfind1)
        rpositions.append(rfind1)

        rfind2 = i.rfind("two")
        # print(rfind2)
        rpositions.append(rfind2)

        rfind3 = i.rfind("three")
        # print(rfind3)
        rpositions.append(rfind3)

        rfind4 = i.rfind("four")
        # print(rfind4)
        rpositions.append(rfind4)

        rfind5 = i.rfind("five")
        # print(rfind5)
        rpositions.append(rfind5)

        rfind6 = i.rfind("six")
        # print(rfind6)
        rpositions.append(rfind6)

        rfind7 = i.rfind("seven")
        # print(rfind7)
        rpositions.append(rfind7)

        rfind8 = i.rfind("eight")
        # print(rfind8)
        rpositions.append(rfind8)

        rfind9 = i.rfind("nine")
        # print(rfind9)
        rpositions.append(rfind9)

        print(rpositions)

        findlast = rpositions.index(max([i for i in rpositions if i >= 0]))

        # print(findlast)

        if findlast == 10 or findlast == 0 :
            lastdigit = char2
        elif 0 < findlast < 10 :
            lastdigit = findlast
        else: print('uh oh')
        
        # print(lastdigit)

        # Concatenate the two digits to make a two-digit number
        twodigits = int(str(firstdigit) + str(lastdigit))
        print(twodigits)

        sum = sum + twodigits

    print(f"The sum is {sum}")
       
file.close()

        



