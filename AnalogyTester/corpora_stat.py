__author__ = 'svobik'


fileName = "/media/data/korpusy/Brychcin-wiki-kategorie/wiki-filteredMIN10.txt"
def f6(seq):
   # Not order preserving
   uniques = set(seq)
   print "Vocab: "+ str(len(uniques))

   return

if __name__ == '__main__':

    words_count = 0.0
    lines_count = 0.0
    list = []
    with open(fileName, 'rb') as f:
        for line in f:
            lines_count = lines_count + 1
            currLine=line
            lines = line.strip().split("\t")
            if (len(lines)>1):
                list.append(lines[1])
                words_count += len(lines[1].strip().split(";"))


    f.close()
    print "Total words count: "+ str(words_count)
    print "Avg. words per article: "+ str(words_count/lines_count)
    f6(list)