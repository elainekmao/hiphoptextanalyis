import csv, math, string, sys, numpy

f = csv.reader(open("tfidf_matrix.csv", 'rb'))
matrix = []
for row in f:
    matrix.append(row)

value_list = []
for i in range(0,134):
    for j in range(i,134):
        if i!= j:
            value = float(matrix[i][j].split()[1][:-1])
            value_list.append(value)

mean = numpy.average(value_list)
median = numpy.median(value_list)

print "Mean: " + str(mean)
print "Median: " + str(median)