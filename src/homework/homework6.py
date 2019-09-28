from ast import literal_eval as make_tuple
"""DO NOT USE LISTS


Create a function get_point_mutations that accepts two string parameters, dna_string1 and dna_string2 and returns
the hamming distance of the strings.,

Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.
See link http://rosalind.info/problems/hamm/ for more information.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset (function parameter)
Parameter dna_string1: GAGCCTACTAACGGGAT
Parameter dna_string2: CATCGTAATGACGGCCT

Sample Output (function return value)
7
"""


def get_point_mutations(dna_string1, dna_string2):
    hamming_distance = 0
    for char in range(0, len(dna_string1)):
        if dna_string1[char] != dna_string2[char]:
            hamming_distance += 1

    return hamming_distance


'''
DO NOT USE LISTS
Create a function get_dna_complement with a dna string parameter that returns the reverse complement of the dna string.

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the
complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
See link for more information http://rosalind.info/problems/revc/.

Given: A DNA string

Return: The reverse complement of the dna string

Sample Dataset (function parameter)
dna_string:  AAAACCCGGT

Sample Output(function return value)
ACCGGGTTTT
'''


def get_dna_complement(dna_string):

    complement_dna_string = ''

    for ch in range(0, len(dna_string)):
        if dna_string[ch] == 'A':
            complement_dna_string = 'T' + complement_dna_string
        elif dna_string[ch] == 'T':
            complement_dna_string = 'A' + complement_dna_string
        elif dna_string[ch] == 'G':
            complement_dna_string = 'C' + complement_dna_string
        elif dna_string[ch] == 'C':
            complement_dna_string = 'G' + complement_dna_string

    return complement_dna_string


'''
DO NOT USE LISTS
Create a function transcribe_dna_into_rna with a dna_string parameter that returns the rna of the string.

Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing 
all occurrences of 'T' in t with 'U' in u.
See link for more information http://rosalind.info/problems/rna/.

Given: A DNA string t having length at most 1000

Return: The transcribed RNA string of t.

Sample Dataset (function parameter)
dna_string: GATGGAACTTGACTACGTAAATT

Sample Output (function return value)
GAUGGAACUUGACUACGUAAAUU
'''


def transcribe_dna_into_rna(dna_string):

    rna_string = ''

    for char in range(0, len(dna_string)):
        if dna_string[char] == 'T':
            rna_string += 'U'
        else:
            rna_string += dna_string[char]

    return rna_string


'''
DO NOT USE LISTS:

Create a function named get_gc_content with a string parameter named dna_string that returns gc content of dna.

PROBLEM
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example,
the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is
called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some
labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates
the label of the next string.
See link for more information http://rosalind.info/problems/gc/. 

Given: a DNA string (function parameter)

Return: The gc content of DNA string (function return value)

Sample Dataset:
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT

Sample output:
60.91954
'''


def get_gc_content(dna_string):

    gc_count = 0
    string_length = len(dna_string)

    for char in range(0, string_length):
        if dna_string[char] == 'G' or dna_string[char] == 'C':
            gc_count += 1

    gc_content = float(gc_count)/float(string_length) * 100.0

    return round(gc_content, 5)


"""
DO NOT USE LISTS

THIS IS OPTIONAL

Create a function get_most_likely_ancestor_conensus with two string parameters dna_string1 and dna_string2 that
returns the beginning position of occurences of dna_string2 in dna_string1.

Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s 
(as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the 
positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position 
i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the 
substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it 
occurs more than once as a substring of s (see the Sample below).

See link for more information http://rosalind.info/problems/subs/.

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset (Function parameters)
parameter dna_string1: GATATATGCATATACTT
parameter dna_string2: ATAT

Sample Output(function return value)
2 4 10
"""

def get_most_likely_ancestor_conensus(dna_string1, dna_string2):

    result_list = ''
    for i in range(0, len(dna_string1)):
        sub_1 = dna_string1[i:i+len(dna_string2)]
        if sub_1 == dna_string2:
            result_list += str(i+1) + ','
    return make_tuple(result_list)


"""
DO NOT USE LISTS
THIS IS OPTIONAL
Create a function get_consenus_from_dna with 7 dna string parameters that returns 5 values consenus, profilea, profilec,
profileg, profilet

Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given 
a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in 
which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents 
the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each 
position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the 
profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus 
strings.

DNA Strings	
A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T

Profile A   5 1 0 0 5 5 0 0
Profile	C   0 0 1 4 2 0 6 1
Profile G   1 1 6 3 0 1 0 0
Profile T   1 5 0 0 0 1 1 6

Consensus
A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then 
you may return any one of them.)

Sample Dataset(function parameters)
dna_string1: ATCCAGCT
dna_string2: GGGCAACT
dna_string3: ATGGATCT
dna_string4: AAGCAACC
dna_string5: TTGGAACT
dna_string6: ATGCCATT
dna_string7: ATGGCACT

Sample Output:
return value 1 Consensus: A T G C A A C T 
return value 2 A: 5 1 0 0 5 5 0 0
return value 3 C: 0 0 1 4 2 0 6 1
return value 4 G: 1 1 6 3 0 1 0 0
return value 5 T: 1 5 0 0 0 1 1 6


"""

def get_consenus_from_dna(dna_string1, dna_string2, dna_string3, dna_string4, dna_string5, dna_string6, dna_string7):

    consensus = ''
    profilea = ''
    profilet = ''
    profileg = ''
    profilec = ''
    for i in range(0, len(dna_string1)):
        int_profilea = 0
        int_profilet = 0
        int_profileg = 0
        int_profilec = 0
        char = dna_string1[i]
        if char == 'A':
            int_profilea += 1
        elif char == 'C':
            int_profilec += 1
        elif char == 'G':
            int_profileg += 1
        elif char == 'T':
            int_profilet += 1

        char2 = dna_string2[i]
        if char2 == 'A':
            int_profilea += 1
        elif char2 == 'C':
            int_profilec += 1
        elif char2 == 'G':
            int_profileg += 1
        elif char2 == 'T':
            int_profilet += 1

        char3 = dna_string3[i]
        if char3 == 'A':
            int_profilea += 1
        elif char3 == 'C':
            int_profilec += 1
        elif char3 == 'G':
            int_profileg += 1
        elif char3 == 'T':
            int_profilet += 1

        char4 = dna_string4[i]
        if char4 == 'A':
            int_profilea += 1
        elif char4 == 'C':
            int_profilec += 1
        elif char4 == 'G':
            int_profileg += 1
        elif char4 == 'T':
            int_profilet += 1

        char5 = dna_string5[i]
        if char5 == 'A':
            int_profilea += 1
        elif char5 == 'C':
            int_profilec += 1
        elif char5 == 'G':
            int_profileg += 1
        elif char5 == 'T':
            int_profilet += 1

        char6 = dna_string6[i]
        if char6 == 'A':
            int_profilea += 1
        elif char6 == 'C':
            int_profilec += 1
        elif char6 == 'G':
            int_profileg += 1
        elif char6 == 'T':
            int_profilet += 1

        char7 = dna_string7[i]
        if char7 == 'A':
            int_profilea += 1
        elif char7 == 'C':
            int_profilec += 1
        elif char7 == 'G':
            int_profileg += 1
        elif char7 == 'T':
            int_profilet += 1

        profilea += str(int_profilea) + ' '
        profilet += str(int_profilet) + ' '
        profileg += str(int_profileg) + ' '
        profilec += str(int_profilec) + ' '

        if int_profilec > int_profilea and int_profilec > int_profileg and int_profilec > int_profilet:
            consensus += 'C' + ' '

        if int_profilet > int_profilec and int_profilet > int_profileg and int_profilet > int_profilea:
            consensus += 'T' + ' '

        if int_profilea > int_profilet and int_profilea > int_profileg and int_profilea > int_profilec:
            consensus += 'A' + ' '

        if int_profileg > int_profilec and int_profileg > int_profilet and int_profileg > int_profilea:
            consensus += 'G' + ' '

    return 'Consensus: ' + consensus, 'A: ' + profilea, 'C: ' + profilec, 'G: ' + profileg, 'T: ' + profilet





