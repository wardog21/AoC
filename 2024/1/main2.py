with open("input.txt") as file:
	lines = file.readlines()

left = []
right = []

for line in lines:
	temp = line.split('   ')
	left.append(int(temp[0]))
	right.append(int(temp[1]))
left.sort()
right.sort()

result = 0

for a in left:
	result += right.count(a) * a

print(result)