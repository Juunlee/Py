import csv
import time 
import panphon
import panphon.distance
dst = panphon.distance.Distance()

Header = []
all_language_vectors = []
with open('abvd_lang_ipa.csv', mode='r', encoding = 'utf-8') as infile:
    with open('abvd_vectors.csv', mode = 'w', encoding = 'utf-8', newline = '\n') as outfile:
        reader = csv.reader(infile, delimiter = ',')
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header_row = next(reader)
        writer.writerow(header_row)
        num = 0
        new_time = time.time()
        for row in reader:
            old_time = new_time
            lang_name = row[0]
            Header.append(row[0])
            outrow = [lang_name]
            for word in row[1:]:
                outrow.append(dst.fm.word_to_vector_list(word, numeric=True))
            writer.writerow(outrow)
            all_language_vectors.append(outrow)
            new_time = time.time()
            print("language", num, "took", new_time - old_time, "seconds to extract vectors")
            num+=1
            if num>=6:
                break


difference_matrix = []
def compute_differences():
    for i in range(len(all_language_vectors)):
        for j in range(len(all_language_vectors)):
            if len(all_language_vectors[i][1:]) != len(all_language_vectors[j][1:]):
                print("Length match error i=", i, "j=", j)
                return
    new_time = time.time()
    for i in range(len(all_language_vectors)):
        old_time = new_time
        difference_matrix.append([])
        for j in range(len(all_language_vectors)):
            distances = []
            for k in range(len(all_language_vectors[i][1:])):
                #use k+1 to index into it
                distances.append(dst.min_edit_distance(dst.unweighted_deletion_cost,
                                          dst.unweighted_insertion_cost,
                                          dst.unweighted_substitution_cost,
                                          [[]],
                                          all_language_vectors[i][k+1],
                                          all_language_vectors[j][k+1]))
            difference = sum(distances)/len(distances)
            difference_matrix[-1].append(difference)
        new_time = time.time()
        print("language", i, "took", new_time - old_time, "seconds to compare with to vector")
    with open('abvd_distances_2.csv', mode = 'w', encoding = 'utf-8', newline = '\n') as outfile:
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #For the first row, replace all the numbers by using Header list
        #Use pop to pop out the first number in csv and replace it with the corresponding language.
        for row in difference_matrix:
            writer.writerow(row)
        
compute_differences()
