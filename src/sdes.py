""" Module pour chiffrer un texte de taille 8bits avec SDES """

KEY_LENGTH = 10
SUB_KEY_LENGTH = 8
DATA_LENGTH = 8
FLENGTH = 4

# Tables for initial and final permutations (b1, b2, b3, ... b8)
IPtable = (2, 6, 3, 1, 4, 8, 5, 7)
FPtable = (4, 1, 3, 5, 7, 2, 8, 6)

# Tables for subkey generation (k1, k2, k3, ... k10)
P10table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8table = (6, 3, 7, 4, 8, 5, 10, 9)

# Tables for the feistel_subkey function
EPtable = (4, 1, 2, 3, 2, 3, 4, 1)
S0table = (1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 3, 1, 3, 2)
S1table = (0, 1, 2, 3, 2, 0, 1, 3, 3, 0, 1, 0, 2, 1, 0, 3)
P4table = (2, 4, 3, 1)

def perm(input_byte, perm_table):
    """Permute input byte according to permutation table"""
    output_byte = 0
    for index, elem in enumerate(perm_table):
        if index >= elem:
            output_byte |= (input_byte & (128 >> (elem - 1))) >> (index - (elem - 1))
        else:
            output_byte |= (input_byte & (128 >> (elem - 1))) << ((elem - 1) - index)
    return output_byte

def initial_permutation(input_byte):
    """Perform the initial permutation on data"""
    return perm(input_byte, IPtable)

def final_permutation(input_byte):
    """Perform the final permutation on data"""
    return perm(input_byte, FPtable)

def swap_nibbles(input_byte):
    """Swap the two nibbles of data"""
    return (input_byte << 4 | input_byte >> 4) & 0xff

def key_gen(key):
    """Generate the two required subkeys"""
    def left_shift(key_bit_list):
        """Perform a circular left shift on the first and second five bits"""
        shifted_key = [None] * KEY_LENGTH
        shifted_key[0:9] = key_bit_list[1:10]
        shifted_key[4] = key_bit_list[0]
        shifted_key[9] = key_bit_list[5]
        return shifted_key

    # Converts input key (integer) into a list of binary digits
    key_list = [(key & 1 << i) >> i for i in reversed(range(KEY_LENGTH))]
    perm_key_list = [None] * KEY_LENGTH
    for index, elem in enumerate(P10table):
        perm_key_list[index] = key_list[elem - 1]
    shifted_once_key = left_shift(perm_key_list)
    shifted_twice_key = left_shift(left_shift(shifted_once_key))
    sub_key1 = sub_key2 = 0
    for index, elem in enumerate(P8table):
        sub_key1 += (128 >> index) * shifted_once_key[elem - 1]
        sub_key2 += (128 >> index) * shifted_twice_key[elem - 1]
    return (sub_key1, sub_key2)

def feistel_subkey(sub_key, input_data):
    """Apply Feistel function on data with given subkey"""
    def feistel(s_key, right_nibble):
        aux = s_key ^ perm(swap_nibbles(right_nibble), EPtable)
        index1 = ((aux & 0x80) >> 4) + ((aux & 0x40) >> 5) + \
                 ((aux & 0x20) >> 5) + ((aux & 0x10) >> 2)
        index2 = ((aux & 0x08) >> 0) + ((aux & 0x04) >> 1) + \
                 ((aux & 0x02) >> 1) + ((aux & 0x01) << 2)
        sbox_outputs = swap_nibbles((S0table[index1] << 2) + S1table[index2])
        return perm(sbox_outputs, P4table)

    left_nibble, right_nibble = input_data & 0xf0, input_data & 0x0f
    return (left_nibble ^ feistel(sub_key, right_nibble)) | right_nibble

def encrypt(key, plaintext):
    """Encrypt plaintext with given key"""
    data = feistel_subkey(key_gen(key)[0], initial_permutation(plaintext))
    return final_permutation(feistel_subkey(key_gen(key)[1], swap_nibbles(data)))

def decrypt(key, ciphertext):
    """Decrypt ciphertext with given key"""
    data = feistel_subkey(key_gen(key)[1], initial_permutation(ciphertext))
    return final_permutation(feistel_subkey(key_gen(key)[0], swap_nibbles(data)))
