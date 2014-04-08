import csv, math, string, collections, operator

years = collections.defaultdict(str)

csv.field_size_limit(1000000000)

with open('west_coast_by_year.csv', 'rb') as csvfile:
    lyrics = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in lyrics:
        if row[0] not in years:
            years[row[0]] = row[1]
        else:
            years[row[0]] += ' ' + row[1]

sortedyears = sorted(years.keys())

with open('sorted_west.csv', 'w') as output:
    f = csv.writer(output, delimiter=',', quotechar='"')
    for year in sortedyears:
        f.writerow([year, years[year]])
