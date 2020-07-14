from feature_edit_distance_lists import avg_fed_list
from feature_edit_distance_lists import fed_list
import csv
import panphon

def words_distance(languages,lang1, lang2):
    for row in languages:
        if row[0] == lang1:
            language1 = row[1:]
        if row[0] == lang2:
            language2 = row[1:]
    return fed_list(language1, language2)

def avg_words_distance(languages, lang1, lang2):
    language1 = None
    language2 = None
    for row in languages:
        if row[0] == lang1:
            language1 = row[1:]
        if row[0] == lang2:
            language2 = row[1:]
    if not language1:
        print('ERROR: ',lang1, 'not found')
        return
    if not language2:
        print('ERROR: ', lang2, 'not found')
        return
    return avg_fed_list(language1, language2)

def min_words_distance(languages, lang1, lang2):
    for row in languages:
        if row[0] == lang1:
            language1 = row[1:]
        if row[0] == lang2:
            language2 = row[1:]
    return min(fed_list(language1, language2))

def third(somelist):
    return somelist[2]

def min_avg_words_distance(languages):
    list_of_averages = []
    for i in range(len(languages)):
        for j in range(i+1, len(languages)):
            language1 = languages[i][0]
            language2 = languages[j][0]
            language1data = languages[i][1:]
            language2data = languages[j][1:]
            list_of_averages.append([language1,language2, avg_fed_list(language1data , language2data)])
    return min(list_of_averages, key = third)

def min_nondiag_triple(matrix):
    """Returns a triple consisting of a row #, col#, and value
    of a minimal non-diagnol entry of matrix."""
    if (not len(matrix) > 1) or (not len(matrix[0]) > 1):
        print("Error in min_nondiag_positive_triple: matrix too small")
        return 
    minval = matrix[0][1]
    mini = 0
    minj = 1 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] < minval:
                 mini, minj, minval = i, j, matrix[i][j]
                 #print('mini', mini, 'minj', minj, 'minval', minval)
    return mini, minj, minval

def load_languages(filename, delimiter=',', language_list = ['N/A']):
    languages = []
    with open(filename, encoding = 'utf-8') as f:
        reader = None
        reader = csv.reader(f, delimiter = delimiter)
        header_row = next(reader)
        header_len = len(header_row)
        languages = []
        for row in reader:
            if len(row) != len(header_row):
                print("row of length", len(row),
                      "does not match, header of length", header_len)
            else:
                languages.append(row)
                if language_list!= 'N/A':
                    language_list.append(row[0])
    f.close()
    return languages

    
if __name__ == "__main__":
    option_num = input("Type1 or 2:")
    filename = None
    if int(option_num)==1:
        filename = 'languages.csv'
        delimiter = '\t'
    elif int(option_num)==2:
        filename = 'Alanguage.csv'
        delimiter = ','
    else:
        print("Error:invalid input")
    languages = load_languages(filename, delimiter)
    #print(min_avg_words_distance(languages))
    #print("What languages do you want to compare?")
    #lang1 = input("Language1:")
    #lang2 = input("Language2:")
    #print(words_distance(lang1,lang2))
    #print(avg_words_distance(languages, lang1, lang2))
    #print(min_words_distance(languages, lang1, lang2))
    languagelist = []
    if int(option_num) == 1:
        languagelist = ['Spanish', 'English', 'Serbo-Croatian','Polish', 'Tocharian B'] 
    elif int(option_num) == 2:
        languagelist = ['Ilocano', 'Malay', 'Tagalog', 'Cebuano', 'Pampangan']
    matrixy = []
    for i in range(len(languagelist)):
        matrixy.append([])
        for j in range(len(languagelist)):
            distancey = avg_words_distance(languages, languagelist[i], languagelist[j])
            roundy = round(distancey, 2)
            matrixy[-1].append(roundy)
    print(matrixy)
