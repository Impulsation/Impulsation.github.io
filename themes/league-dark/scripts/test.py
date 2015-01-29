f = open('new.txt', 'r')

for line in f:
	print line
	line.strip()
	print line