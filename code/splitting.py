import csv
import sys
import random

try:
	P = float( sys.argv[1] )
except IndexError:
	P = 0.9
	
print "P = %s" % ( P )

input_file = 'clean_input.csv'
output_file1 = 'trainA.csv'
output_file2 = 'trainB.csv'

i = open( input_file )
o1 = open( output_file1, 'wb' )
o2 = open( output_file2, 'wb' )

reader = csv.reader( i )
writer1 = csv.writer( o1 )
writer2 = csv.writer( o2 )

#headers = reader.next()
#writer1.writerow( headers )
#writer2.writerow( headers )

for line in reader:
	r = random.random()
	if r > P:
		writer2.writerow( line )
	else:
		writer1.writerow( line )
