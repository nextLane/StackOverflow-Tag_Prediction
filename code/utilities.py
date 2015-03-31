import csv

def labelling( status ):
	labels = ['not a real question', 'not constructive', 'off topic', 'open', 'too localized']
	label = labels.index( status ) + 1
	return label

def get_data(clean_csv_file):
	reader = csv.reader( open( input_file ) )
	return reader

def get_closed(clean_csv_file, labels=[], first=-1):
	data = get_data(clean_csv_file)
	results = []
	if len(labels) is 0:
		for index, each_row in enumerate(data):
			if each_row[1] != 4:
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

def get_closed(clean_csv_file, first=-1):
	data = get_data(clean_csv_file)
	results = []
	if len(labels) is 0:
		for index, each_row in enumerate(data):
			if each_row[1] == 4:
				results.append(each_row)
			if first != -1 and index >= first:
				break
