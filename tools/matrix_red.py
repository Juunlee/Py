from feature_edit_distance_lists import avg_fed_list
from feature_edit_distance_lists import fed_list
import csv
import panphon


def red_matrix(matrix,i,j):
    "The function that returns the matrix with average distance"
    Mmatrix = []
    for q in range(len(matrix)):
        Mmatrix.append(matrix[q])
        avg = (matrix[q][i] + matrix[q][j])/2
        Mmatrix[q].pop(j)
        Mmatrix[q].pop(i)
        Mmatrix[q].append(avg)
    NewM = average_of_lists(Mmatrix[i], Mmatrix[j])
    Mmatrix.pop(j)
    Mmatrix.pop(i)
    Mmatrix.append(NewM)
    return Mmatrix

def average_of_lists(list1, list2):
    list3 = []
    for a in range(len(list1)):
        summ = (list1[a] + list2[a])/2
        list3.append(summ)
    return list3

if __name__== "__main__":
    matrixy = [[0.0, 1.1, 1.04, 0.83, 0.66], [1.1, 0.0, 1.07, 0.97, 0.97], [1.04, 1.07, 0.0, 0.22, 0.84],
              [0.83, 0.97, 0.22, 0.0, 0.76], [0.66, 0.97, 0.84, 0.76, 0.0]]
    print(matrixy)

    listt = [2,3,4]
    listtt = [4,5,6]

    print(red_matrix(matrixy,2,3))
    print(average_of_lists(listt,listtt))
