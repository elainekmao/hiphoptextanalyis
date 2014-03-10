import csv, math, string, sys
from gensim import corpora, models, similarities

corpus = corpora.MmCorpus('hiphop_corpus.mm')
dictionary = corpora.Dictionary.load('hiphop.dict')

tfidf = models.TfidfModel(corpus, normalize=True)
tfidf_corpus = tfidf[corpus]
tfidf_index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=47897)

tfidf.save('tfidf_model.tfidf')
tfidf_index.save('tfidf.index')

i = 0
for document in tfidf_corpus:
    total_writer = csv.writer(open('results/total_tfidf.csv', 'a'))
    total_writer.writerow(document)
    i += 1
    if i in range(1,76):
        w = csv.writer(open('results/east_coast_tfidf.csv', 'a'))
        w.writerow(document)
    elif i in range(76,89):
        w = csv.writer(open('results/midwest_tfidf.csv', 'a'))
        w.writerow(document)
    elif i in range(89,116):
        w = csv.writer(open('results/south_tfidf.csv', 'a'))
        w.writerow(document)
    elif i in range(116,151):
        w = csv.writer(open('results/west_coast_tfidf.csv', 'a'))
        w.writerow(document)
print "TF-IDF done."

lsi = models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=300)
lsi_corpus = lsi[tfidf_corpus]
lsi_index = similarities.MatrixSimilarity(lsi_corpus)

lsi.save('lsi_model.lsi')
lsi_index.save('lsi.index')

i = 0
for document in lsi_corpus:
    total_writer = csv.writer(open('results/total_lsi.csv', 'a'))
    total_writer.writerow(document)
    i += 1
    if i in range(1,76):
        w = csv.writer(open('results/east_coast_lsi.csv', 'a'))
        w.writerow(document)
    elif i in range(76,89):
        w = csv.writer(open('results/midwest_lsi.csv', 'a'))
        w.writerow(document)
    elif i in range(89,116):
        w = csv.writer(open('results/south_lsi.csv', 'a'))
        w.writerow(document)
    elif i in range(116,151):
        w = csv.writer(open('results/west_coast_lsi.csv', 'a'))
        w.writerow(document)
print "LSI done."