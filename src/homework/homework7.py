'''
Problem
For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the
proportion of corresponding symbols that differ between s1 and s2.

For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings),
 we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given
in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that
your answer is allowed an absolute error of 0.001.

Sample Dataset
[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Sample Output
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000

'''


def get_distance_matrix(dna_list):
    d = empty_matrix(len(dna_list))
    for i in range(0, len(dna_list)):
        for j in range(0, len(dna_list)):
            result = dp(dna_list[i], dna_list[j])
            d[i][j] = result
    return d


#creates square matrix
def empty_matrix(rows):
    a = [0] * rows
    for i in range(rows):
        a[i] = [0] * rows
    return a


def dp(dna_list1, dna_list2):
    difference = 0
    for i in range(0, len(dna_list1)):
        if dna_list1[i] != dna_list2[i]:
            difference += 1
        else:
            difference += 0
    return difference/len(dna_list1)

