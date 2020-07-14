import csv
import time 
import panphon
import panphon.distance
dst = panphon.distance.Distance()

def min_edit_distance(self, del_cost, ins_cost, sub_cost, start, source, target):
    """Return minimum edit distance, parameterized, slow
    Args:
        del_cost (function): cost function for deletion
        ins_cost (function): cost function for insertion
        sub_cost (function): cost function for substitution
        start (sequence): start symbol: string for strings, list for lists,
                          list of list for list of lists
        source (sequence): source string/sequence of feature vectors
        target (sequence): target string/sequence of feature vectors
    Returns:
        Number: minimum edit distance from source to target, with edit costs
                as defined
    """
    # Get lengths of source and target
    n, m = len(source), len(target)
    source, target = start + source, start + target
    # Create "matrix"
    d = []
    for i in range(n + 1):
        d.append((m + 1) * [None])
    # Initialize "matrix"
    d[0][0] = 0
    for i in range(1, n + 1):
        d[i][0] = d[i - 1][0] + del_cost(source[i])
    for j in range(1, m + 1):
        d[0][j] = d[0][j - 1] + ins_cost(target[j])
    # Recurrence relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min([
                d[i - 1][j] + del_cost(source[i]),
                d[i - 1][j - 1] + sub_cost(source[i], target[j]),
                d[i][j - 1] + ins_cost(target[j]),
            ])
    return d[n][m]

if __name__ == "__main__":
    vec1 = dst.fm.word_to_vector_list("bʊk", numeric = True)
    vec2 = dst.fm.word_to_vector_list("ʃɹt", numeric = True)
    print(dst.min_edit_distance(dst.unweighted_deletion_cost,
                                          dst.unweighted_insertion_cost,
                                          dst.unweighted_substitution_cost,
                                          [[]],
                                          vec1,
                                          vec2))
                          
    for i in range(len(vec1)):
        print(dst.unweighted_deletion_cost(vec1[i]))
        print(dst.unweighted_insertion_cost(vec1[i]))
        print(dst.unweighted_deletion_cost(vec2[i]))
        print(dst.unweighted_insertion_cost(vec2[i]))
