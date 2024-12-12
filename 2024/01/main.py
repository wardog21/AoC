with open("01/input.txt") as file:
	lines = file.readlines()

left = []
right = []

for line in lines:
	temp = line.split('   ')
	left.append(int(temp[0]))
	right.append(int(temp[1]))
left.sort()
right.sort()

result = [abs(a-b) for a, b in zip(left,right)]

print(sum(result))