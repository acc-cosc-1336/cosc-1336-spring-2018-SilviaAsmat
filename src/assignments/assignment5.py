def recursive_decimal_binary(num, bits):

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
    carry = True
    for index in range(7, -1, -1):
        char = bits_list[index]
        if char == '0' and carry == True:
            bits_list[index] = '1'
            final_string = ''.join(bits_list)
            return final_string
        elif char == '0' and carry == False:
            final_string = ''.join(bits_list)
            return final_string
        elif char == '1' and carry == False:
            final_string = ''.join(bits_list)
            return final_string
        elif char == '1' and carry == True:
            bits_list[index] = '0'
    final_string = ''.join(bits_list)
    return final_string









