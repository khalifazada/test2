import csv

print('Question 6 Python:\n')

with open('file.txt', 'r') as file:
	text = file.read()
	print(text)

with open('python.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',')
	csv_writer.writerow(text)

print('CSV created')

