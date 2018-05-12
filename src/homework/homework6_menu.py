from src.homework.homework6 import get_dna_complement
from src.homework.homework6 import get_gc_content
from src.homework.homework6 import get_point_mutations
from src.homework.homework6 import transcribe_dna_into_rna
from src.homework.homework6 import get_most_likely_ancestor_conensus
from src.homework.homework6 import get_consenus_from_dna

#write import statements for homework 6 functions


def menu_options():
    print()
    print('1) Point Mutations')
    print('2) DNA Complement')
    print('3) DNA to RNA')
    print('4) GC Content')
    print('5) DNA motif')
    print('6) Most likely Ancestor')
    print('7) Exit')
    print()


def run_menu():

    option = -1

    while option != 7:
        menu_options()
        option = int(input("Enter menu choice: "))

        while option < 1 or option > 7:
            print("Valid menu range 1-7")
            option = int(input("Enter menu choice: "))

        if option == 1:
            handle_option_1()
        elif option == 2:
            handle_option_2()
        elif option == 3:
            handle_option_3()
        elif option == 4:
            handle_option_4()
        elif option == 5:
            handle_option_5()
        elif option == 6:
            handle_option_6()


def handle_option_1():
    '''
    Write code to:
    Loop as long as user wants to continue.
    Prompt user for two dna strings of length 10 with letter range A,C,G, and T only.  
    Call the function get_point_mutations and display the mutations to screen.
    Ask user if they want to continue.
    '''
    continue_loop = 'Y'
    while continue_loop == 'Y':
        dna_string_1 = input('Enter DNA string 1: ')
        
        while len(dna_string_1) != 10:
            dna_string_1 = input('Enter DNA string 1: ')
        
        dna_string_2 = input('Enter DNA string 2: ')
        
        while len(dna_string_2) != 10:
            dna_string_2 = input('Enter DNA string 2: ')
        
        mutations = get_point_mutations(dna_string_1, dna_string_2)
        print(mutations)
        continue_loop = input('Enter Y to continue')
#validate dna_string_1 and dna_string_2


def handle_option_2():
    '''
    Write code to read the file dna_complement.dat.
    For each line string call the function get_dna_complement and display the complement to screen.
    '''

    dna_complement_object = open('dna_complement.dat', 'r')
    for line in dna_complement_object:
        dna_complement = get_dna_complement(line)
        print(dna_complement)
    dna_complement_object.close()


def handle_option_3():
    '''
    Write the code to read the file transcribe_dna_to_rna.dat.
    For each line string call the function transcribe_dna_to_rna and display rna to screen.
    '''
    transcribe_file_object = open('transcribe_dna_to_rna.dat', 'r')
    for line in transcribe_file_object:
        rna_string = transcribe_dna_into_rna(line)
        print(rna_string)
    transcribe_file_object.close()

def handle_option_4():
    '''
    Write code to read the file compute_gc_content.dat and for each line
    call the get_gc_content function with the line string as an argument.
    Display the gc_content for each line.
    '''
    compute_gc_object = open('compute_gc_content.dat', 'r')
    for line in compute_gc_object:
        gc_content = get_gc_content(line)
        print(gc_content)
    compute_gc_object.close()

def handle_option_5():
    dna_string1 = input('Enter dna_string1')
    dna_string2 = input('Enter dna_string2')
    result = get_most_likely_ancestor_conensus(dna_string1, dna_string2)
    print(result)

def handle_option_6():

    dna_string1 = input('Enter dna_string1')
    dna_string2 = input('Enter dna_string2')
    dna_string3 = input('Enter dna_string3')
    dna_string4 = input('Enter dna_string4')
    dna_string5 = input('Enter dna_string5')
    dna_string6 = input('Enter dna_string6')
    dna_string7 = input('Enter dna_string7')

    result = get_consenus_from_dna(dna_string1, dna_string2, dna_string3, dna_string4, dna_string5, dna_string6, dna_string7)
    print(result)
