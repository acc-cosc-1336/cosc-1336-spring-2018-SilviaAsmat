def recursive_decimal_binary(num, bits='00000000'):

    '''
    Given a whole number from the decimal system, converts the number to 8-bit binary
    Given 86 returns 01010110
    :param num:
    :return:
    '''
    if num == 0:
        return bits
    else:
        # need to add 1 to bits
        bits_plus_one = add_one_to_bits(bits)
        return recursive_decimal_binary(num -1, bits_plus_one)

def add_one_to_bits(bits):
    bits_list = list(bits)
    #list() turns bits string into an index?
    carry = True
    #'00000000' is bits, as a string?
    #use range to go from right to left of the 8-bit binary string,(7,-1,-1)
    for index in range(7, -1, -1):
        char = bits_list[index]
        #carry being the next bit in sequence if 1 already occupies the spot.
        if char == '0' and carry == True:
            bits_list[index] = '1'
            final_string = ''.join(bits_list)
            return final_string
        #final_string is the fully converted num into binary
        elif char == '0' and carry == False:
            final_string = ''.join(bits_list)
            #.join() brings together the seperate parts of the string
            #ex: '0'+'0'+'1'+'1' becomes 0011 because of .join()
            return final_string
        elif char == '1' and carry == False:
            final_string = ''.join(bits_list)
            return final_string
        elif char == '1' and carry == True:
            bits_list[index] = '0'
    final_string = ''.join(bits_list)
    return final_string









