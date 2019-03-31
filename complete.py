file = open("log.txt")

newList = []
for i, line in enumerate(file):
    if(i % 2 == 0):
        newList.append(line[6:14])

k = 0

print("X" + "\t" + "Y" + '\t' + "Correct Output" + "\t" + "Simulated Output" + "   Result")
print("----------------------------------------------------------------------------------")
for i in range(0,16):
    for j in range(0,16):
	if(format(i*j, '#010b')[2:] == newList[k]):
		print(format(i, '#06b')[2:] + "\t" + format(j, '#06b')[2:] + '\t' + format(i*j, '#010b')[2:] + "\t" + newList[k] + "\t" + "Correct")
	else:
		print(format(i, '#06b')[2:] + "\t" + format(j, '#06b')[2:] + '\t' + format(i*j, '#010b')[2:] + "\t" + newList[k] + "\t" + "Wrong")
	k = k + 1
