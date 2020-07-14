import csv

with open('abvd_distances_updated.csv', mode = 'w', encoding = 'utf-8', newline = '\n') as outfile:
    with open('abvd_distances2.csv', mode = 'r', encoding = 'utf-8') as infile:
        with open('eliminating_languages.csv', mode = 'r', encoding = 'utf-8') as infile2:
            reader = csv.reader(infile, delimiter = ',')
            reader2 = csv.reader(infile2, delimiter = ',')
            writer = csv.writer(outfile, delimiter = ',')
            Header = next(reader)
            langindices = next(reader2)
            for i in range(len(langindices)):
                langindices[i] = int(langindices[i])
            for num in langindices:
                Header.pop(num+1)
            writer.writerow(Header)
            A = 0
                
            for row in reader:
                if A in langindices:
                    A +=1
                    continue
                print(len(row))
                A +=1
                #if A > 1:
                    #break
                for num in langindices:
                    row.pop(num+1)

                print(len(row))
        
                writer.writerow(row)
