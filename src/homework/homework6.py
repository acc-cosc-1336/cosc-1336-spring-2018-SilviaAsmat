'''
DO NOT USE LISTS

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
'''

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


'''
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
'''

'''
DO NOT USE LISTS
THIS IS OPTIONAL
Create a function get_consenus_from_dna with 7 dna string parameters that returns 5 values consenus, profilea, profilec,
profilet, profilet

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
dna_string8: ATGCAACT

Sample Output:
return value 1 Consensus: A T G C A A C T 
return value 2 A: 5 1 0 0 5 5 0 0
return value 3 C: 0 0 1 4 2 0 6 1
return value 4 G: 1 1 6 3 0 1 0 0
return value 5 T: 1 5 0 0 0 1 1 6


'''
