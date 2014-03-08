import csv, math, string, sys

east = csv.reader(open("east_coast_tfidf.csv", 'rb'), delimiter=",")
midwest = csv.reader(open("midwest_tfidf.csv", 'rb'), delimiter=",")
south = csv.reader(open("south_tfidf.csv", 'rb'), delimiter=",")
west = csv.reader(open("west_coast_tfidf.csv", 'rb'), delimiter=",")