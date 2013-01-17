# Python
# breaks large data file into chunks

path = "../Processed_Data/Without_Accession/"
source_file = "narrative_strings_only.txt"

target_files = []
for i in range(1, 10):
    target_files.append("narratives%d.txt" % i)

print "Path: ", path
print "Opening source: ", source_file
source = open(path + source_file, 'r')

for target_file in target_files:
    print "Opening target: ", target_file
    target = open(path + target_file, 'w')
    
    count = 0
    line = source.readline()
    while line:
        target.write(line + '\n')
        count += 1
        if count >= 13500:
            print count, "lines written to target."
            count = 0
            break
        line = source.readline() 
    
    print "Closing target."
    target.close()

print "Closing source."
source.close()

print "\nAll done."
