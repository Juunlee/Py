from feature_edit_distance_lists import avg_fed_list
from feature_edit_distance_lists import fed_list
import csv
import panphon

filename = 'languages.csv'
languages = []

with open(filename, encoding = 'utf-8') as f:
    reader = csv.reader(f, delimiter = '\t')
    header_row = next(reader)
    header_len = len(header_row)
    languages = []
    for row in reader:
        if len(row) != len(header_row):
            print("row of length", len(row),
                  "does not match, header of length", header_len)
        else:
            languages.append(row)

def words_distance(lang1, lang2):
    for row in languages:
        if row[0] == lang1:
            language1 = row[1:]
        elif row[0] == lang2:
            language2 = row[1:]
    return fed_list(language1, language2)

def avg_words_distance(lang1, lang2):
    for row in languages:
        if row[0] == lang1:
            language1 = row[1:]
        elif row[0] == lang2:
            language2 = row[1:]
    return avg_fed_list(language1, language2)

def min_words_distance(lang1, lang2):
    for row in languages:
        if row[0] == lang1:
            language1 = row[1:]
        elif row[0] == lang2:
            language2 = row[1:]
    return min(fed_list(language1, language2))

def third(somelist):
    return somelist[2]

def min_avg_words_distance():
    list_of_averages = []
    for i in range(len(languages)):
        for j in range(i+1, len(languages)):
            language1 = languages[i][0]
            language2 = languages[j][0]
            language1data = languages[i][1:]
            language2data = languages[j][1:]
            list_of_averages.append([language1,language2, avg_fed_list(language1data , language2data)])
    return min(list_of_averages, key = third)

if __name__ == "__main__":
    print(min_avg_words_distance())
    print("What languages do you want to compare?")
    lang1 = input("Language1:")
    lang2 = input("Language2:")
    print(words_distance(lang1,lang2))
    print(avg_words_distance(lang1, lang2))
    print(min_words_distance(lang1, lang2))
