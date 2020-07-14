import csv
import time 
import panphon
import panphon.distance
dst = panphon.distance.Distance()

language_name = []
Data = []
with open('abvd_lang_ipa.csv', mode='r', encoding = 'utf-8') as infile:
    with open('distances2.csv', mode = 'r', encoding = 'utf-8') as infile2:
        reader = csv.reader(infile, delimiter = ',')
        reader2 = csv.reader(infile2, delimiter = ',')
        header_row = next(reader)
        for row in reader:
            next_row = next(reader2)
            language_name.append(row[0])
            Data.append(next_row[0:])

with open('abvd_distances2.csv', mode = 'w', encoding = 'utf-8', newline = '\n') as outfile:
     writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
     languages = ['Language']
     languages.extend(language_name)
     writer.writerow(languages)
     for i in range(len(language_name)):
         rowrow = [language_name[i]]
         rowrow.extend(Data[i])
         writer.writerow(rowrow)

