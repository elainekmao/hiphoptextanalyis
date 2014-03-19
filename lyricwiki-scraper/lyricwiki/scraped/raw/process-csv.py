import csv, string, sys, re 

def main (f, out):
    i = 0
    j = 0
    with open(f, 'rb') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
        with open(out, 'wb') as outputfile:
            outputwriter = csv.writer(outputfile, delimiter=',')
            for row in filereader:
                if row != ['', '', '', ''] and row != ['album', 'artist', 'lyrics', 'title']:
                    date = get_date(row[0])
                    lyrics = remove_parenthetical(row[2])
                    if date:
                        outputwriter.writerow([date, row[1], lyrics])
                        i += 1
                    else:
                        outputwriter.writerow([None, row[1], lyrics])
                        j += 1
    print "There were " + str(i) + " songs written with year information, " + str(j) + " without."

def get_date(album):
    date = ''
    for i in range(len(album)):
        if album[i] == '(' and str.isdigit(album[i+1]):
            date += album[i+1:i+5]
    if len(date) >= 4:
        date = date[0:4]
    return date

def remove_parenthetical(string):
    return re.sub('[\(\[].*?[\)\]]', '', string)

if __name__ == "__main__": main(sys.argv[1], sys.argv[2])