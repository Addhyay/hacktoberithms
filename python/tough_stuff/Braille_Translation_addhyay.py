import re

def filter(rank):
    """int -> list

    Returns the list of index.

    >>> filter(12):
    [1, 2, 3]
    >>> filter(2):
    [1, 2]
    >>> filter(23):
    [2, 4, 5, 6]
    """
    language = {'a':[0], 'b':[0, 1], 'c':[0, 3], 'd':[0, 3, 4], 'e':[0, 4], 'f':[0, 1, 3], 'g':[0, 1, 3, 4], 'h':[0, 1, 4], 'i':[1, 3], 'j':[1, 3, 4]}
    #this language dictonary contain basic Braille codes, all other codes for alphabets can be derived from these
    if rank in range(0, 11):                    #This is for basic alphabets range (1 to 10 i.e. 'a' to 'j')
        return language[chr(rank+96)]
    elif rank in range(11, 21):                 #These are from 'k' to 't'
        return language[chr(rank+86)] + [2]
    elif rank == 23:                            #Aplhabet 'w' has special case so we give it seprate condition
        return language[chr(rank+76)] + [5]
    elif rank in range(21, 27):                 #These are from 'u' to 'z' except 'w'
        return language[chr(rank+76)] + [2, 5]
    return []                                   #This is the condition when user input character other than 'a' to 'z'

def braille(word):
    """str -> str

    Return the 0 | 1 code using braille code language

    >>> braille('code')
    100100101010100110100010
    >>> braille('harish')
    110010100000111010010100011100110010
    """
    final_output = ''

    letters = re.findall('.', word)             #This is used to seprate all alphabets of the given word
    for every_letter in letters:
        code = ['0', '0', '0', '0', '0', '0']
        rank = ord(every_letter)-96             #Here we calculate rank of the alphabet from word (example: a have rank 1 and likewise)
        if rank < 0 and rank+96 != 32:          #Here we check if alphabet is capital or small and it is not space (ASCII value: 32)
            rank = ord(every_letter)-64
            final_output += '000001'
        idx = filter(rank)                      #Here we receive idx (index list) of respective alphabet
        for index in idx:
            code[index] = '1'                   #Then we mark every zero with indices mentioned in idx (index list) to one in code list
        final_output += ''.join(code)           #Then we join the code of each alphabet and return the complete word code
        final_output += ' '
    return final_output

if __name__=='__main__':
    word = input('ENter sign: ')
    code = braille(word)
    print(code)