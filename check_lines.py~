# Python script: for use in cleaning the data.
# when an irregularity is found, indicates the accession number
# and the number of entries already processed
# waits for user input to continue.

source_path = "../Processed_Data/Full_Data_Cleaned/ASRS2_EVENT_DATA_cleaned_Aug07.TXT"

source = open(source_path, 'r')

i = 1
line = source.readline()

while line:
    fields = line.split('~')
    print i, fields[0]
    if len(fields) < 24:
        print len(fields)
        raw_input("Ready? ")
    line = source.readline()
    i += 1

source.close()


# 107524 Congressman's speech
