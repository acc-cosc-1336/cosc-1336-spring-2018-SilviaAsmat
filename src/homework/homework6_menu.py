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

def handle_option_2():
    '''
    Write code to read the file dna_complement.dat.
    For each line string call the function get_dna_complment and display the complement to screen.
    '''

def handle_option_3():
    '''
    Write the code to read the file transcribe_dna_to_rna.dat.
    For each line string call the function transcribe_dna_to_rna and display rna to screen.
    '''

def handle_option_4():
    '''
    Write code to read the file compute_gc_content.dat and for each line
    call the get_gc_content function with the line string as an argument.
    Display the gc_content for each line.
    '''

def handle_option_5():
    pass #optional 

def handle_option_6():
    pass #optional
