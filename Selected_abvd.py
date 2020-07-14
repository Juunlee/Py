import csv

indices = [733, 734, 508, 23, 285, 151, 84, 49, 167, 138, 184, 148, 3, 105, 19, 274, 261, 258,
           242, 1340, 102, 35, 62, 135, 317, 310, 81, 279]
with open('selected_abvd.csv', mode = 'w', encoding = 'utf-8', newline = '\n') as outfile:
    with open('abvd_lang_ipa.csv', mode = 'r', encoding = 'utf-8') as infile:
        reader = csv.reader(infile, delimiter = ',')
        header = next(reader)
        writer = csv.writer(outfile)
        i = 0
        for row in reader:
            i+=1
            if i+1 in indices:
                writer.writerow(row)


    
