from src.homework.homework7 import get_distance_matrix


#write import statement for homework 7 file

'''
Write a main function to...
Read p_distance.dat file
From the file data, create a two-dimensional list like the following example:

[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Pass the list to the get_p_distance_matrix function as an argument
Display the p distance matrix to screen
'''


def main():
    dp = open('p_distance.dat', 'r')
    dna_list = []
    for line in dp.readlines():
        line = line.replace('\n', '')
        line = line.strip()
        line_result = line.split(' ')
        dna_list.append(line_result)
    dp.close()
    result = get_distance_matrix(dna_list)

    for i in range(0, len(result)):
        print(result[i])


main()