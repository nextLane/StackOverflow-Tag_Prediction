import sys, csv

hashmap = {1:'not a real question', 2:'not constructive', 3:'off topic', 4:'open', 5:'too localized'}
input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'wb' )

