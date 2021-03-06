# This python script assembles a slice of the data.
# Created data file is a list of accession number-keyword field pairs
# Script can be modified to create a list of accession-narrative pairs, etc.

source_name = "../Processed_Data/Full_Data_Cleaned/ASRS2_EVENT_DATA_cleaned_Aug07.TXT"
target_name = "event_accession_synopsis.txt"

source = open(source_name, 'r')
target = open(target_name, 'w')

print "Reading and writing data."

line = source.readline()

while line:
    fields = line.split('~')
    #print fields[0]
    if len(fields) > 0:
        # depending on which field you want--->V
        newline = '~'.join([fields[0], fields[-3]]) + '\n'
        target.write(newline)
    line = source.readline()


source.close()
target.close()

print "All done!"
