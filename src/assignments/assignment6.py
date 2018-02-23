def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for i in range(0, len(dna_string)):
        char = dna_string[i]
        if char == 'A':
            a_count += 1
        if char == 'C':
            c_count += 1
        if char == 'G':
            g_count += 1
        if char == 'T':
            t_count += 1
    return a_count, c_count, g_count, t_count





