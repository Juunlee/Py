import numpy as np
import csv
import panphon
import panphon.distance
dst = panphon.distance.Distance()

num_langs = 9
num_words = 114
num_iters = 1000
loud = False

def random_pairing(d,i,j,n):
    g = np.full(n,-1)
    for h in range(n):
        c = np.random.permutation(d[:,j]) #random permutation of jth language
        e = 0 #running total
        for k in range(len(d)):
            e += dst.levenshtein_distance(d[k][i],c[k])
        g[h]=e
    #print(g)
    return np.mean(g),np.std(g)

def find_distance(row, i, j):
    #return round(dst.dolgo_prime_distance(row[i+1],row[j+1])/(len(dst.map_to_dolgo_prime(row[i+1]))+len(dst.map_to_dolgo_prime(row[j+1]))+1),2)
    #if i==9 and j==6:
    #    print("row[9+1,0]:",row[i+1][0],
    #          "row[6+1,0]:",row[j+1][0],
    #          "distance:",dst.dolgo_prime_distance(row[i+1][0],row[j+1][0]))
    return dst.dogol_prime_distance(row[i+1][0],row[j+1][0])

def output_prime_transcriptions(dt, line_count, s):
    output_string = f'{dt[line_count-1]}'
    for i in range(num_langs):
        output_string += s[i]+'\t'    
    print(output_string)

def output_stats_from_all_random_pairings(ds, swadesh_list_table):
    final_table = np.zeros((num_langs,num_langs))
    for y in range(num_langs):
        for z in range(num_langs):
            i=random_pairing(swadesh_list_table,y,z,num_iters)
            z_score = (i[0]-ds[y][z])/i[1]
            print(str(y),str(z),i,z_score)
            final_table[y][z]=round(z_score,2)
    print(final_table)

index_list = [63, 64, 46, 72, 66, 73, 44, 82, 67, 0, 47, 21, 68, 6, 1, 77, 76, 22, 11,
              100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]

def special_sum(dt_array, index_list):
    # sums the entries in dt_array at indices from index_list.
    return dt_array[index_list].sum(axis=0)

with open('Swadesh - 114 word list.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    dt = np.full((num_words,num_langs,num_langs),-1) # distance table
    swadesh_list_table = np.full((num_words,num_langs),'U') # 'U' for undefined
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif line_count <= num_words:
            s=['']*num_langs
            for i in range(num_langs):
                s[i]=dst.map_to_dogol_prime(row[i+1])
                for j in range(num_langs):
                    dt[line_count-1][i][j] = find_distance(row, i, j)
                    #if i==9 and j==6:
                    #    print("Yoruba:",row[i+1],"=",s[i],
                    #          "Hindi:",row[j+1],"=",s[j],
                    #          "Distance:",dt[line_count-1][i][j])
            swadesh_list_table[line_count-1]=np.asarray(s)
            if loud:
                output_prime_transcriptions(dt,line_count,s)
            line_count += 1
    #print(dt)
    dt_array = np.array(dt)
    ds = dt_array.sum(axis=0) # distance sums
    dss = special_sum(dt_array, index_list) # special sum of distances; using Baxter's 33 words.
    print(ds)
    print(dss)
    print(swadesh_list_table)
    #output_stats_from_all_random_pairings(ds, swadesh_list_table)
    output_stats_from_all_random_pairings(dss, swadesh_list_table[index_list])
    print(f'Processed {line_count} lines.')


