# # not wokring
# from functools import cache

# @cache
# def generateMovements(input, pos):
#     myString = ""
#     positions = {
#         '^': (0,1),
#         '<': (1,0),
#         'v': (1,1),
#         '>': (1,2),
#         'A': (0,2)
#     }
#     diffY = positions[input][0] - positions[pos][0]
#     diffX = positions[input][1] - positions[pos][1]
#     if positions[input][1] == 0:
#         for ii in range(diffY):
#             myString += 'v'
#         for ii in range(-diffX):
#             myString += '<'
#     else:
#         if diffX < 0:
#             for ii in range(-diffX):
#                 myString += '<'
#         if diffY > 0:
#             for ii in range(diffY):
#                 myString += 'v'
#         if diffY < 0:
#             for ii in range(-diffY):
#                 myString += '^'
#         if diffX > 0:
#             for ii in range(diffX):
#                 myString += '>'
#     myString += 'A'
#     return myString

# directionalKeys = ['<','v','^','>','A']
# movements = {}
# movements7 = {}

# for goal in directionalKeys:
#     for start in directionalKeys:
#         movements.update({goal+start:generateMovements(goal,start)})

# @cache
# def directionalKeypadHelper(input):
#     myString = ""
#     pos = 'A'

#     for i in range(len(input)):
#         myStr = movements[input[i]+pos]
#         # myStr = directionalKeypadHelper(input[i], pos)
#         pos = input[i]
#         myString += myStr
#     return myString

# counter = []
# counting = True
# for i in range(8):
#     counter.append(0)
# while counting:
#     inputStr = ""
#     for i in range(len(counter)):
#         inputStr += directionalKeys[counter[i]]
#         movements7.update({inputStr: directionalKeypadHelper(inputStr)})
#     counter[0] += 1
#     for i in range(len(counter)):
#         if counter[i] == 5:
#             if i == len(counter)-1:
#                 counting = False
#                 break
#             else:
#                 counter[i] = 0
#                 counter[i+1] += 1
#     # print(inputStr)


# def directionalKeypad(input):
#     myString = ""
#     pos = 'A'

#     for i in range(len(input)//7):
#         myString += movements7[input[7*i:7*i+7]+pos]
#         # myStr = directionalKeypadHelper(input[i], pos)
#         pos = input[i*7+6]
#     for i in range(len(input)-len(input)//7, len(input)):
#         myString += movements[input[i]+pos]
#         pos = input[i]
#     return myString

# def numericKeypad(input):
#     myString = ""
#     pos = 'A'
#     positions = {
#         '0': (3,1),
#         '1': (2,0),
#         '2': (2,1),
#         '3': (2,2),
#         '4': (1,0),
#         '5': (1,1),
#         '6': (1,2),
#         '7': (0,0),
#         '8': (0,1),
#         '9': (0,2),
#         'A': (3,2)
#     }
#     for i in range(len(input)):
#         diffY = positions[input[i]][0] - positions[pos][0]
#         diffX = positions[input[i]][1] - positions[pos][1]
#         if positions[input[i]][1] == 0 and positions[pos][0] == 3:
#             for ii in range(-diffY):
#                 myString += '^'
#             for ii in range(-diffX):
#                 myString += '<'
#         elif positions[input[i]][0] == 3 and positions[pos][1] == 0:
#             for ii in range(diffX):
#                 myString += '>'
#             for ii in range(diffY):
#                 myString += 'v'
#         else:
#             if diffX < 0:
#                 for ii in range(-diffX):
#                     myString += '<'
#             if diffY > 0:
#                 for ii in range(diffY):
#                     myString += 'v'
#             if diffY < 0:
#                 for ii in range(-diffY):
#                     myString += '^'
#             if diffX > 0:
#                 for ii in range(diffX):
#                     myString += '>'
#         pos = input[i]
#         myString += 'A'
        
#     return myString

# with open("21/input.txt") as file:
#     puzzle = file.readlines()

# result = 0
# for code in puzzle:
#     print(code)
#     sequence = numericKeypad(code.strip())
#     for i in range(15):
#         print(i,len(sequence))
#         sequence = directionalKeypad(sequence)
#     result += len(sequence) * int(code.strip()[:-1])
#     print(len(sequence), int(code.strip()[:-1]), len(sequence) * int(code.strip()[:-1]))
# print(result)