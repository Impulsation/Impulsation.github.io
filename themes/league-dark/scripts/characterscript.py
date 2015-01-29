f = open('new.txt', 'r')
o = open('new2.txt', 'w')
i = 1

for line in f:
	line = line.strip()
	print line
	line.replace(" ", "")
	print line
	o.write("\"%s\", \n" % (line))
	i += 1
f.close()
o.close()