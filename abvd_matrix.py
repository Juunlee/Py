import csv

num_langs = 1637

language_name_list = []
Head_row = ["Language"]
vocab_matrix = []
for i in range(num_langs):
    with open('abvd/lang'+str(i+1)+'.csv') as f:
        reader = csv.reader(f, delimiter = ',')
        header_row = next(reader)
        second_row = next(reader)
        language_name_list.append(second_row[1])
        vocab_list = []
        vocab_list_found = False 
        for row in reader:
            if vocab_list_found == True:
                vocab_list.append(row[1:4])
                if i==0  and row[2] != Head_row[-1]:                 
                    Head_row.append(row[2])
            if len(row)>=4 and row[0] == 'id' and row[1] == 'word_id' and row[2] == 'word' and row[3] == 'item':
                vocab_list_found = True
        #print(Head_row)
            #print(row)
        vocab_matrix.append(vocab_list)
        #print(vocab_list_found)


hand_tally = 0
for i in range(num_langs):
    #print(language_name_list[i])
    #print(vocab_matrix[i])
    #if vocab_matrix[i][0][1] == 'hand':
        hand_tally += 1 
#print(hand_tally)

abvd = []
for i in range(num_langs):
    # Make a matrix that contains in row i the name of the ith languages
    # and at least one attestation for each of the 210 basic words
    # that are attested in that language
    austronesian = ["" for i in range(211)]
    austronesian[0] = language_name_list[i]
    for entry in vocab_matrix[i]:
        # entry is guaranteed to be a three-element list.
        # first is the word's id number, third is the word in the given language
        index = int(entry[0])
        if austronesian[index] == "":
            austronesian[index] = entry[2]
    abvd.append(austronesian)

with open('abvd_lang.csv', mode='w', encoding = 'utf-8', newline = '') as lang_file:
    lang_writer = csv.writer(lang_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    lang_writer.writerow(Head_row)
    for i in range(num_langs):
        lang_writer.writerow(abvd[i])
