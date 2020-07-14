import csv
from feature_edit_distance_lists import *
from lang_comparison2 import *
import os.path
from os import path 

num_langs = 1637

"""Head_row = ["Languages"]
for i in range(num_langs):
    with open('abvd/lang'+str(i+1)+'.csv', encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter = ',')
        try:
            header_row = next(reader)
            second_row = next(reader)
            Head_row.append(second_row[1])
        except Exception:
            print(i)
print(len(Head_row))
#name = Head_row.pop(0)
name = Head_row[0]
language_list = Head_row[1:]
print(len(language_list))"""

def UPGMA_csv(filename, listOfRows, language_list):
    languages = load_languages(filename, language_list=language_list)
    #return languages
    avg = []
    for i in listOfRows:#range(len(language_list)):
        if i>1636:
            print("Done!")
            return avg
        avg.append([])
        for j in range(len(language_list)):
            try:
                avg[-1].append(avg_fed_list(languages[i][1:], languages[j][1:]))
            except Exception:
                avg[-1].append("")
                #print("Error at i=" + str(i)+", j="+str(j))
                #print(Exception)
                #return avg 
        avg[-1].insert(0, language_list[i])
    #print(avg)
    return(avg)

language_list = []

languages = None
if not path.exists("abvd__l.csv"):
    with open('abvd__l.csv', mode='w', encoding = 'utf-8', newline = '\n') as lang_file:
        languages = load_languages("abvd_lang_ipa.csv", language_list=language_list)
        Head_row = ["Languages"]
        for language in languages:
            Head_row.append(language[0])
        lang_writer = csv.writer(lang_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        lang_writer.writerow(Head_row)
        

num_recorded = 0
with open('abvd__l.csv', mode='r', encoding = 'utf-8') as lang_file:
    reader = csv.reader(lang_file, delimiter = ',')
    header_row = next(reader)
    for row in reader:
        num_recorded += 1
how_many = int(input("How many rows would you like to make today?"))
averages = UPGMA_csv('abvd_lang_ipa.csv',range(num_recorded, num_recorded+ how_many), language_list)
with open('abvd__l.csv', mode='a', encoding = 'utf-8', newline = '\n') as lang_file:
    lang_writer = csv.writer(lang_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(averages)):
        lang_writer.writerow(averages[i])
