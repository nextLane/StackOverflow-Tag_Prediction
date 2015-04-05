import sys, csv, math


hashmap = {1:'not a real question', 2:'not constructive', 3:'off topic', 4:'open', 5:'too localized'}

def sigmoid(x):
	return 1 / (1 + math.exp(-x))
  
def normalize( predictions ):
	s = sum( predictions )
	normalized = []
	for p in predictions:
		normalized.append( p / s )
	return normalized  
   
  
input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'wb' )

reader = csv.reader( i, delimiter = " " )
writer = csv.writer( o )

for line in reader:
	
	probs = []
	for element in line:
		pieces = element.split(':')
		if len(pieces) is 2:
			prediction = pieces[1]
			prob = sigmoid( float( prediction ))
			probs.append( prob )
		elif len(pieces) is 1:
			post_id = int( pieces[0] )

	new_line = normalize( probs )
	
	
	writer.writerow( [post_id] )
	print hashmap[new_line.index(max(new_line))+1], post_id
	writer.writerow( new_line )
