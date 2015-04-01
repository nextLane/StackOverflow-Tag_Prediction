import csv

input_file = 'clean_input.csv'

# reader = csv.reader( open( input_file ) )

def labelling( status ):
	labels = ['not a real question', 'not constructive', 'off topic', 'open', 'too localized']
	label = labels.index( status ) + 1
	return label

def get_reader(clean_csv_file):
	reader = csv.reader( open( input_file ) )
	return reader

def get_closed(clean_csv_file, labels=[], first=-1):
	data = get_reader(clean_csv_file)
	results = []
	if len(labels) is 0:
		for index, each_row in enumerate(data):
			if each_row[1] != '4':
				results.append(each_row)
			if first != -1 and index >= first:
				break
	if len(labels):
		selected = [labelling(label) for label in labels]
		for index, each_row in enumerate(data):
			if each_row[1] in selected:
				results.append(each_row)
			if first != -1 and index >= first:
				break
		
	return results

def get_closed_count(clean_csv_file, labels=[], first=-1):
	return len(get_closed(clean_csv_file, labels, first))

def get_open(clean_csv_file, first=-1):
	data = get_reader(clean_csv_file)
	results = []
	for index, each_row in enumerate(data):
		if each_row[1] == '4':
			results.append(each_row)
		if first != -1 and index >= first:
			break
	return results

def get_open_count(clean_csv_file, first=-1):
	return len(get_open(clean_csv_file, first))

def get_total_count(clean_csv_file):
	reader = get_reader(clean_csv_file)
	return len([row for row in reader])

"""
a = get_closed_count(input_file)
b = get_open_count(input_file)
c = get_total_count(input_file)
print 'CLOSED', a
print 'OPEN', b
print 'TOTAL', c
print 'SURE?', a+b == c
"""
