from feature_edit_distance_lists import avg_fed_list
import csv 

filename = 'languages.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter ='\t')
    header_row = next(reader)
    header_len = len(header_row)
    languages = []
    language1 = []
    language2 = []
    language3 = []
    
    for row in reader:
        if len(row) != len(header_row):
            print("row of length", len(row),
                  "does not match, header of length", header_len)
        else:
            languages.append(row)
            if row[0] == 'Bulgarian':
                language1= row[1:]
            elif row[0] == 'Polish':
                language2=row[1:]
            elif row[0] == 'Russian':
                language3 =row[1:]
                
print(languages)
print('language1', language1)
print('language2',language2)
print('language3', language3)
print(avg_fed_list(language1, language2))

answer_matrix = []
for language1 in languages:
    answer_matrix.append([])
    for language2 in languages:
        #print( 'Now comparing', language1[0], 'to', language2[0])
        try:
            answer = avg_fed_list(language1[1:], language2[1:])
            answer_matrix[-1].append(answer)
        except AttributeError:
            answer_matrix[-1.].append(-1)
    formatted_answer = ""
    for j in range(len(languages)):
        formatted_answer +="{:.2f}".format(answer_matrix[-1][j])+ " "
    print(formatted_answer)
