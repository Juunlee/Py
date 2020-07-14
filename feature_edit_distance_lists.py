import panphon.distance 
dst = panphon.distance.Distance()
from feature_edit_distance_new import feature_edit_distance2 
from matplotlib import pyplot as plt
import numpy as np

def fed_list(list1, list2, new = False, includelower = 1.0):
    """Given 11 and 12 lists of strings of the same length,
    computes a list consisting of the feature edit distance
    between corresponding pairs."""
    if len(list1)!=len(list2):
        print("In fed_list: lists must be of the same length")
        return []
    list3 = []
    for i in range(len(list1)):
        if list1[i] != "" and list2[i]!="":
            if new:
                list3.append(feature_edit_distance2(list1[i],list2[i]))
            else:
                list3.append(dst.feature_edit_distance(list1[i],list2[i]))
    cutoff = np.percentile(list3, includelower*100)
    list4 = []
    for item in list3:
        if item <= cutoff:
            list4.append(item)
    return list4

def avg_fed_list(list1, list2, new = False, includelower = 1.0):
    """Given 11 and 12 lists of strings of the same length,
    computes a list consisting of the average feature edit distance
    between corresponding pairs."""
    if len(list1) != len(list2):
        print("In avg_fed_list: lists must be of the same length.")
        return 0
    if len(list1) == 0:
        print("In avg_fed_list: lists must be of positive length.")
        return 0
    list3 = fed_list(list1, list2, new, includelower = includelower)
    return sum(list3)/len(list3)

def avg_fed_list2(list1, list2):
    """Given l1 and l2 lists of strings of the same length,
    sorts the matches into 'good' and 'bad' matches."""
    if len(list1) != len(list2):
        print("In avg_fed_list: lists must be of the same length.")
        return 0
    if len(list1) == 0:
        print("In avg_fed_list: lists must be of positive length.")
        return 0

def display_feds(list1, list2):
    """Given 11 and 12 lists of strings of the same length,
    display a graph of feature edit distances betwen corresponding pairs versus index."""
    if len(list1) != len(list2):
        print("In display_feds: lists must be of the same length")
        return 
    fig = plt.figure(dpi=128, figsize=(10, 6))
    fed_list_answer = fed_list(list1, list2)
    plt.plot(range(len(fed_list_answer)), fed_list_answer, c='red', alpha=0.5)
   
    plt.title("Feature edit distances between corresponding pairs", fontsize = 24)
    plt.xlabel('', fontsize =16)
    #fig.autofmt_xdate()
    plt.ylabel("Distance", fontsize =16)
    plt.tick_params(axis='both', which = 'major', labelsize=16)

    plt.show()

if __name__ == '__main__':
    eng_words = [u'wən', u'tUw', u'θrIy', u'hootenanny'] 
    rus_words = [u'adyin', u'dva', u'tryi', u'']
    print('Using the English and Russian words for one, two, three')
    
    print('[round(44*x) for x in fed_list(eng_words, rus_words)], includelower= 1.0',
          [round(44*x) for x in fed_list(eng_words, rus_words, includelower = 1.0)])
    print('avg_fed_list(eng_words, rus_words), includelower= 1.0', avg_fed_list(eng_words, rus_words, includelower = 1.0))

    print('[round(44*x) for x in fed_list(eng_words, rus_words)], includelower= 0.75',
          [round(44*x) for x in fed_list(eng_words, rus_words, includelower = 0.75)])
    print('avg_fed_list(eng_words, rus_words), includelower= 0.75', avg_fed_list(eng_words, rus_words, includelower = 0.75))

    print('[round(44*x) for x in fed_list(eng_words, rus_words)], includelower= 0.5',
          [round(44*x) for x in fed_list(eng_words, rus_words, includelower = 0.5)])
    print('avg_fed_list(eng_words, rus_words), includelower= 0.5', avg_fed_list(eng_words, rus_words, includelower = 0.5))

    print('[round(44*x) for x in fed_list(eng_words, rus_words)], includelower= 0.25',
          [round(44*x) for x in fed_list(eng_words, rus_words, includelower = 0.25)])
    print('avg_fed_list(eng_words, rus_words), includelower= 0.25', avg_fed_list(eng_words, rus_words, includelower = 0.25))

    print('Running display_feds(eng_words, rus_words).')
    display_feds(eng_words,rus_words)
