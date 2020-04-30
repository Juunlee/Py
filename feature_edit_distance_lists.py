import panphon.distance 
dst = panphon.distance.Distance()
from matplotlib import pyplot as plt

def fed_list(list1, list2):
    """Given 11 and 12 lists of strings of the same length,
    computes a list consisting of the feature edit distance
    between corresponding pairs."""
    if len(list1)!=len(list2):
        print("In fed_list: lists must be of the same length")
        return []
    list3 = []
    for i in range(len(list1)):
        list3.append(dst.feature_edit_distance(list1[i],list2[i]))
    return list3 
def avg_fed_list(list1, list2):
    """Given 11 and 12 lists of strings of the same length,
    computes a list consisting of the average feature edit distance
    between corresponding pairs."""
    if len(list1) != len(list2):
        print("In avg_fed_list: lists must be of the same length.")
        return 0
    if len(list1) == 0:
        print("In avg_fed_list: lists must be of positive length.")
        return 0
    list3 = fed_list(list1, list2)
    return sum(list3)/len(list3)
def display_feds(list1, list2):
    """Given 11 and 12 lists of strings of the same length,
    display a graph of feature edit distances betwen corresponding pairs versus index."""
    if len(list1) != len(list2):
        print("In display_feds: lists must be of the same length")
        return 
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(range(len(list1)), fed_list(list1, list2), c='red', alpha=0.5)
   
    plt.title("Feature edit distances between corresponding pairs", fontsize = 24)
    plt.xlabel('', fontsize =16)
    #fig.autofmt_xdate()
    plt.ylabel("Distance", fontsize =16)
    plt.tick_params(axis='both', which = 'major', labelsize=16)

    plt.show()




if __name__ == '__main__':
    eng_words = [u'wən', u'tUw', u'θrIy']
    rus_words = [u'adyin', u'dva', u'tryi']
    print('Using the English and Russian words for one, two, three')
    print('[round(44*x) for x in fed_list(eng_words, rus_words)]',
          [round(44*x) for x in fed_list(eng_words, rus_words)])
    print('avg_fed_list(eng_words, rus_words)', avg_fed_list(eng_words, rus_words))
    print('Running display_feds(eng_words, rus_words).')
    display_feds(eng_words,rus_words)
