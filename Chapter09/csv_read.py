import csv
 
csv_file = open('Sample - Superstore.csv', 'r', encoding='windows-1252')
with csv_file:
	read_csv = csv.reader(csv_file)
	#for row in read_csv:
		#print(row)
	for index, row in enumerate(read_csv):
		if index <= 5:
			print(row)
