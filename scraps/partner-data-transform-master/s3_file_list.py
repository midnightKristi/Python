import boto3
import csv
import datetime

# Change "BUCKET" to name of bucket we're working in, e.g. 'opaexport-conv'.
s3 = boto3.resource('s3')
bucket = s3.Bucket(name='BUCKET')

# Create the new CSV. Change "output.csv" to set the name of the output CSV file. Set the prefix to use in searching with the "Prefix=" parameter, (currently set to empty).
with open('output.csv', 'wb') as log:
	print(datetime.datetime.now().time())
	writelog = csv.writer(log)
	for obj in bucket.objects.filter(Prefix=''):
		if obj.size > 1:  # Make sure object is a file and not a directory.
			if obj.key.split('.')[-1] != 'xlsx':  # Exclude Excel or text files, which are probably file lists, not digital objects.
				if obj.key.split('.')[-1] != 'txt':
					if 'KEYWORD'.lower() in obj.key.lower():  # Test for keyword matching, and then write a row in the CSV for matches. Change "KEYWORD" to search term.
						writelog.writerow((obj.key, obj.size, obj.key.split('/')[-3], obj.key.split('/')[-1]))
print(datetime.datetime.now().time())
