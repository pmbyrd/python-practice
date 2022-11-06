def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    #loop over each el in the lst if not type of str or int remove

    # for el in lst:
    #     if el is not type(str) or type(int):
    #         lst.remove(el)
    
    # return lst

    # for el in lst:
    #     if el is not el:
    #         lst.remove(el)
    # return lst

    return [el for el in lst if el]
