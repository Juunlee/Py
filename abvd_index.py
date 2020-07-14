import csv

with open('abvd_lang_ipa.csv', mode = 'r', encoding = 'utf-8') as infile:
    reader = csv.reader(infile, delimiter = ',')
    header_row = next(reader)
    entries = ([len(list(filter(None, w))) for w in reader])
    langindex = []
    for number in entries:
        if number < 100:
            langindex.append(entries.index(int(number)))
    indices = sorted(set(langindex))
    indices2 = sorted(indices, reverse = True)
    print(indices2)
    

with open('eliminating_languages.csv', mode = 'w', encoding = 'utf-8', newline = '\n') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(indices2)
    
        
