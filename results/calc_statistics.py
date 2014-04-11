import csv, math, string, sys, numpy

def main(document):
    f = csv.reader(open(document, 'rb'))
    matrix = []
    for row in f:
        matrix.append(row)
    value_list = []
    for i in range(0,150):
        for j in range(i,150):
            if i!= j:
                value = float(matrix[i][j].split()[1][:-1])
                value_list.append(value)
    mean = numpy.average(value_list)
    median = numpy.median(value_list)
    std = numpy.std(value_list)
    print "Mean: " + str(mean)
    print "Median: " + str(median)
    print "Maximum: " + str(max(value_list))
    print "Minimum: " + str(min(value_list))
    print "Standard Deviation: " + str(std)

if __name__ == "__main__": main(sys.argv[1])