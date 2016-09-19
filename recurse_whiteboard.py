"""Recursive function to reverse list.


The function takes two parameters, a list and rev_l, which is also a
list, whose default is set as None.  This will reverse a list, by 
returning rev_l.  This does not reverse a nested list.

"""

def reverse_list(lst, rev_l=None):
    """Reverse list using recursion."""

    if not lst:
        return []

    if rev_l is None:
        rev_l = []
        
    rev_l.append(lst[-1])
    reverse_list(lst[:-1], rev_l)

    return rev_l