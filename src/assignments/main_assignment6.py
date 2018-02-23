from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string

#write the import for the function get_count_A_C_G_and_T_in_string from assignment 6 file

#Using function get_count_A_C_G_and_T_in_string create a main function and...
#Call the function get_count_A_C_G_and_T_in_string from assignment 6 file
#With the string AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC as an argument
#Sample Output:

#DNA String:
#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
#A 20, C 12, G 17, T 21


#Call the main function in Python Shell or in this file.


def main():
    a_count, c_count, g_count, t_count = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    print('A ', a_count, ' C ', c_count, ' G ', g_count, ' T ', t_count)


main()


