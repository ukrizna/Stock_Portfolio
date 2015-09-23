# -*- coding: utf-8 -*-
'''Action Neededd : 1) Please change the filepath as needed (Search for "open" and change the path 2) Please note that this program has been written on a Windows machine'''


#opening the file
with open('\\fileC.txt') as f:
	#parsing each line
	for line in f:
		#removing trailing and leading whitespaces
		cleaned_line = line.strip()
		#checking for existing of lines
		if cleaned_line:
			#finding the ip value in fileC
			f1 = line[line.find('='):line.find(';')]
			#finding the ip given
			f2 = line[line.find(';'):line.find('7990')]
			#cleaning the ip value and converting to integer.
			val = f1[1:]
			val = val.strip()
			val = int(val)
			#cleaning the ip, splitting it and converting to integer.
			ip = f2[1:]
			ip = ip.split('.')
			Y = int(ip[2])
			Z = int(ip[3])
			#applying the formula to calculate ip value from ip i.e. port = W.X.Y.Z =>  50000 + 200(y) + z
			ip_val = 50000 + 200*Y + Z;
			#checking for non-equality
			if (ip_val != val):
				print line, ip_val
			
f.close()