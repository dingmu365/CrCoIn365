# 1. Array and String
# Q1: is_unique


def is_unique_python(input):
    if len(set(input)) == len(input):
        return True
    else:
        return False

def is_unique_char_algorithmic(input):
    if len(input) > 128:
        return False

    char_set = [False] * 128
    # a quick way to initiate an array with a fixed value

    for char in input:
        val = ord(char)  # get the ID of char of ASCII
        if char_set[val]:
            return False
        else:
            char_set[val] = True

        return True

def is_unique_bit_vector(input):
    if len(input) > 128:
        return False
    checker = 0
    for c in input:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val  # |= => equals to +=

def is_unique_set(input):
    character_set=set()
    for c in input:
        if c in character_set:
            return False
        else:
            character_set.add(c)
    return True

def is_unique_sorting(input):
    sorted_input=sorted(input)
    between=None
    for c in sorted_input:
        if c==between:
            return False
        else:
            between=c

    return True