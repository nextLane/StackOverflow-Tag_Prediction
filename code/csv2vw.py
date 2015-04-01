import sys, csv, re

input_file = 'clean_input.csv'
output_file = 'vw_format.vw'

reader = csv.reader( open( input_file ))
o = open( output_file, 'wb' )

def csv_to_vw():

	for count, line in enumerate(reader):
		# print len(line),
		# print line[-1]

		post_id = line[0]
		status = line[1]
		reputation = line[2]
		good_posts = line[3]
		title = line[4]
		tags = line[5:-1]
		body = line[-1]
		tags = " ".join( tags ).strip()

		output_line = "%s %s %s" % ( status, 1, post_id )
		output_line += "|n %s %s" % ( reputation, good_posts )
		output_line += "|ti %s |ta %s |b %s" % ( title, tags, body )
		output_line += "\n"
		o.write( output_line )

csv_to_vw()
