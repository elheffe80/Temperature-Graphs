import csv

ifile = open('Temperatures.csv', "rb")
reader = csv.reader(ifile)
rownum = 0
for row in reader:
	#save header row
	if rownum == 0:
		header = row
	else:
		colnum = 0
		for col in row:
			if col == 0:
				print row[col]
			elif col == 1:
				print row[col]
			elif col == 2:
				print row[col]

	rownum += 1
	
ifile.close()