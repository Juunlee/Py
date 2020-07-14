from feature_edit_distance_lists import * # fed_list(list1, list2) and avg_fed_list(list1, list2), display_feds(list1, list2)
from matrix_red import * #red_matrix(matrix,i, j), average_of_lists(list1, list2)
from tools.node import Node
from lang_comparison2 import *
from tools.save_tree import to_file
from tools.save_XML import XML_node 
#words_distance(languages,lang1, lang2)
#avg_words_distance(languages,lang1, lang2)
#min_words_distance(languages, lang1, lang2), third(somelist)
#load_languages(filename, delimiter = ',')
#min_avg_words_distance(languages)
#min_nondiag_triple(matrix)
from time import process_time 

# We should use fed_list(list1, list2) and avg_fed_list(list1, list2), and min(fed_list
"""Unweighted Pair Group Method with Arithmetic mean"""
"""Sokal & Michener 1958"""


def UPGMA(matrix, names= None) :
    if not names:
        names = [str(i) for i in range(len(matrix))]
    """ Contructs the phylogenetic tree determined by UPGMA
    from the pairwise-distance matrix matrix."""
    if len(matrix)!= len(names):
        print("ERROR: in UPGMA(), matrix and names should be of the same length")
        return None 
    #file = input('Name of the file that you want to make a phylogenetic tree:')
    #langauges = load_languages(file)
    #matrix = []
    #for i in range(len(languages)):
    #    matrix.append([])
    #    for j in range(len(languages)):
    #        distancey = avg_fed_list(languages[i][1:], languages[j][1:])
    #       matrix[-1].append(distancey)
    #print(matrix)
    nodelist = [Node(item) for item in names]
    while len(nodelist)>1:
        mnt = min_nondiag_triple(matrix)
        #print(mnt)
        i = min(mnt[0], mnt[1])
        j = max(mnt[0], mnt[1])
        reduced_matrix = red_matrix(matrix, i, j)
        #print(reduced_matrix)
        new_node = Node(str(round(mnt[2],2)))
        nodelist.append(new_node)
        new_node.insert_left(nodelist[i])
        new_node.insert_right(nodelist[j])
        nodelist.pop(j)
        nodelist.pop(i)
        #for node in nodelist:
        #    print(node)
        matrix = reduced_matrix
    return nodelist[0]

def csv_to_tree(filename,
                index_list = None,
                intermediate_time = None,
                new = False,
                includelower = 1.0):
    """Runs UPGMA on the language data in the csv file at filename.
    Data should be in every row starting with the second row,
    and the first entry of each row should be the language name.
    If index_list is passed in, then uses only languages whose row numbers
    in the csv are two more than the numbers in index_list.
    Use new=true to lower the weight of insertions and delections from 1.0 to 0.5.
    Use includelower = 0.75 to exclude the upper quartile."""
    
    languages = load_languages(filename)
    matrix = []
    names = []
    if not index_list:
        index_list = range(len(languages))
    for i in index_list:
        matrix.append([])
        names.append(languages[i][0])
        for j in index_list:
            distancey = avg_fed_list(languages[i][1:],
                                     languages[j][1:],
                                     new,
                                     includelower = includelower )
            matrix[-1].append(distancey)
    if intermediate_time:
        intermediate_time.append(process_time())
    return UPGMA(matrix, names)


root_node = None
if __name__=="__main__":
    """ with open("abvd_distances_updated.csv", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        header_row = next(reader)
        lang_names = []
        dist_matrix = []
        for row in reader:
            lang_names.append(row[0])
            dist_matrix.append([float(x) for x in row[1:]])
        root_node = UPGMA(dist_matrix, lang_names)
        root_XML = XML_node(root_node)
    with open("abvd.xml",mode = 'w', encoding = "utf-8") as outfile:
        outfile.write(root_XML)
    """
    root_node = csv_to_tree('selected_abvd.csv', includelower = 0.5)
    print('full set',root_node)
    root_XML = XML_node(root_node)
    print('as XML', root_XML)
    with open('selected_abvd12.xml', 'w', encoding = "utf-8") as f:
        f.write(root_XML)
    #print('lower three quartiles',csv_to_tree('oceanic_filipino2.csv', includelower = 0.75))
    #print('lower half',csv_to_tree('oceanic_filipino2.csv', includelower = 0.5))
    #print('lower quartile',csv_to_tree('oceanic_filipino2.csv', includelower = 0.25))
    """i_time = [1]
    for i in range(2,10):
        time1 = process_time()
        print(csv_to_tree("abvd_lang.csv", range(i), intermediate_time=i_time))
        time2 = process_time()
        print("UPGMA took", time2-time1, "seconds for", i, "languages.")
    print("Language comparison took", i_time[-1]-time1, "seconds and matrix computation took", time2-i_time[-1])
languages = load_languages('Alanguage.csv')
    print(avg_words_distance(languages, 'Ilocano', 'Cebuano'))
    print(avg_fed_list(languages[0][1:], languages[3][1:]))
    I = Node("Ilocano")
    M = Node("Malay")
    T = Node("Tagalog")
    C = Node("Cebuano")
    P = Node("Pampangan")
    nodelist = [I, M, T, C, P]
    matrixy = []
    for i in range(len(languages)):
        matrixy.append([])
        for j in range(len(languages)):
            distancey = avg_fed_list(languages[i][1:], languages[j][1:])
            #roundy = round(distancey, 2)
            #matrixy[-1].append(roundy)
            matrixy[-1].append(distancey)
    print(matrixy)
    
    #UPGMA(matrixy, ["Illocano", "Malay", "Tagalog", "Cebuano", "Pampangan"])
mnt = min_nondiag_triple(matrixy)
    print(mnt)
    i = min(mnt[0], mnt[1])
    j = max(mnt[0], mnt[1])
    reduced_matrix = red_matrix(matrixy, i, j)
    print(reduced_matrix)
    new_node = Node("New")
    nodelist.append(new_node)
    new_node.insert_left(nodelist[i])
    new_node.insert_right(nodelist[j])
    nodelist.pop(j)
    nodelist.pop(i)


    mnt2 = min_nondiag_triple(reduced_matrix)
    print(mnt2)
    i = min(mnt2[0], mnt2[1])
    j = max(mnt2[0], mnt2[1])
    reduced_matrix2 = red_matrix(reduced_matrix, i, j)
    print(reduced_matrix2)
    new_node2 = Node("New2")
    nodelist.append(new_node2)
    new_node2.insert_left(nodelist[i])
    new_node2.insert_right(nodelist[j])
    nodelist.pop(j)
    nodelist.pop(i)
    for node in nodelist:
        print(node)
    mnt3 = min_nondiag_triple(reduced_matrix2)
    print(mnt3)"""
