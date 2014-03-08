import csv, math, string, sys
from gensim import corpora, models, similarities

#Increases field size limit
csv.field_size_limit(1000000000)

texts = []
with open('alllyricsbyartist.csv', 'rb') as csvfile:
    docreader = csv.reader(csvfile, delimiter=',')
    for row in docreader:
        document = []
        for word in row[1].split():
            document.append(word)
        texts.append(document)

dictionary = corpora.Dictionary(texts)
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(once_ids)
dictionary.compactify()
dictionary.save('hiphop.dict')
print dictionary

dict_list = []
keys = dictionary.token2id.keys()
values = dictionary.token2id.values()
for item in range(0, len(dictionary)):
    dict_list.append([values[item], keys[item]])
docwriter = csv.writer(open("hiphopdictionary.csv", "wb"))
docwriter.writerows(dict_list)

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('hiphop_corpus.mm', corpus)