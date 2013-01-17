# Python script:
# searches through and counts the number of lines

path = "../Processed_Data/Full_Data_Cleaned/"
filename = "ASRS2_EVENT_DATA_cleaned_Aug07.TXT"
source_path = path + filename

source = open(source_path, 'r')


print "Counting the lines in the file..."

count = 0
line = source.readline()

while line:
    count += 1
    line = source.readline()

source.close()

print "Document: %s" % filename
print "Path: %s" % path
print "Line Count: %d" % count

# count is 121122
# explanation: 1 heading, 121121 records
