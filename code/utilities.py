import csv, re


def get_words( text ):
	# Preprocesses the text and converts them to lower case words.
	text = text.replace( "'", "" )
	text = re.sub( r'\W+', ' ', text )
	text = text.lower()
	
	text = text.split()
	words = []
	for w in text:
		if w in words:
			continue
		words.append( w )
		
	words = " ".join( words )
	return words

def process_tags( tag ):
	# Removes the shit out of tags and makes them lower case.
	tag = re.sub( r'\W+', '', tag )
	tag = tag.lower()
	return tag


input_file = '../data/train_sample.csv'
output_file = 'output.csv'

reader = csv.reader( open( input_file ) )
writer = csv.writer( open( output_file, 'wb') )


# Ignoring headers in the data files
headers = reader.next()

for index, row in enumerate(reader):
	# uncomment the next line to see if it works and then CTRL-C
	# print index, row

	post_id = row[0]
	try:
		post_status = row[14]
	except IndexError:
		post_status = 0

	reputation = row[4]
	good_posts = row[5]

	title = get_words( row[6] )
	body = get_words( row[7] )
	tags = row[8:13]
	tags = list( set( map( process_tags, tags ) ) )

	writer.writerow( [ post_id, post_status, reputation, good_posts, title] + tags + [ body ] )

	# Uncomment the next 2 lines if you don't want to know shit !
	if not index % 1000 :
		print index, [ post_id, post_status, reputation, good_posts, title] + tags + [ body ]
