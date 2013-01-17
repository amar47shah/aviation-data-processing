# Python script: retrieve data by accession number

source_path = "../Processed_Data/Full_Data_Cleaned/ASRS2_EVENT_DATA_cleaned_Aug07.TXT"

source = open(source_path, 'r')

query = raw_input("Accession number without final '.00'? ")
query += '.00'

line = source.readline()

while line:
    fields = line.split('~')
    if query == fields[0]:
        print line
        break
    line = source.readline()


source.close()


# 107524 Congressman's speech
