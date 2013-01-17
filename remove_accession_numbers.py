# Python Script
# Removes accession numbers from a one-dimension-with-accession data file


source_name = "../Processed_Data/One_Dimension_with_Accession_Numbers/event_accession_synopsis.txt"
target_name = "synopsis_strings_only.txt"

source = open(source_name, 'r')
target = open(target_name, 'w')

print "Reading and writing data."

line = source.readline()

while line:
    fields = line.split('~')
    #print fields[0], fields[-1]
    target.write(fields[-1])
    line = source.readline()


source.close()
target.close()

print "All done!"
