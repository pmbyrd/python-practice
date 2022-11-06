def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
        # empty dict
    # counter = {}
    # # loop over ltr
    # for ltr in phrase:
    #     counter[ltr] = counter.get(ltr, 0) + 1

    # return counter

    #need to make the numbers iterable

    count1 = {}
    count2 = {}
    str_num1 = str(num1)
    str_num2 = str(num2)

    


