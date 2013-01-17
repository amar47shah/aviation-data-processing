from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text

corpus_root = "/home/amar/Documents/DataMiningLab/Aviation_Data/Processed_Data/Without_Accession"
filename = "keywords_strings_only.txt"
aviation = PlaintextCorpusReader(corpus_root, '.*')
event_text = Text(aviation.words(filename))
# Now event_text is a Text object.

from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text

corpus_root = "/home/amar/Documents/DataMiningLab/Aviation_Data/Processed_Data/Without_Accession"

texts=[]
aviation = PlaintextCorpusReader(corpus_root, '.*')
for filename in aviation.fileids():
    texts.append(Text(aviation.words(filename)))

# Now Texts is a list of Text objects.
