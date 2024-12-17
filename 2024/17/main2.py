# # # not working

# import functools
# command = [2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0]

# @functools.cache
# def calc(regA):
#     regB = regA % 8
#     regB = regB ^ 5
#     regC = int( regA // (1 << regB) )
#     regB = regB ^ regC
#     regA = int( regA // 8 )
#     regB = regB ^ 6
#     output = regB % 8
#     return regA, output

# for i in range(10000000):
#     output = []
#     found = False

#     while True:
#         i, out = calc(i)
#         output.append(out)

#         if len(output) > 0:
#             found = True
#             for i in range(len(output)):
#                 if command[i] != output[i]:
#                     found = False
#                     break
#             if not found: continue
#         if len(output) == len(command) and found:
#             break
    
#     if found:
#         print(i)
#         break