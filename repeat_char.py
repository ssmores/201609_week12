"""Function to return first non-repeating character in string."""

def first_non_rep(string):
    """Finds first non-repeating character in string.

    >>> first_non_rep('a')
    'a'

    >>> first_non_rep('abbati')
    't'

    >>> first_non_rep('Aaa')
    

    >>> first_non_rep('')
    

    """
    if len(string) == 0:
        return None

    if len(string) == 1:
        return string

    letter_dict = {}
    # Letters in the string will get appended to the list, so order is maintained.
    one_char = []

    for letter in string:
        letter = letter.lower() 
        if letter in letter_dict:
            letter_dict[letter] += 1
            if letter in one_char:
                one_char.remove(letter)
        else:
            letter_dict[letter] = 1
            one_char.append(letter)
    if not one_char:
        return None
    else:
        return one_char[0]




############################################
# Doctests will run if this is run directly.
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print