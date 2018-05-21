title="temp"
outfile = open("{0}.txt".format(title),"w")
with open("Jay_Chou.txt","r") as file:
	for line in file:
		line = line.strip()
		if len(line) == 0:
			continue
		if ":" in line:
			continue
		#print(line)
		if line[0] == "~":
			outfile.close()
			title = line.strip("~")
			outfile = open("{0}.txt".format(title),"w")
		else:
			outfile.write(line+"\n")

			
