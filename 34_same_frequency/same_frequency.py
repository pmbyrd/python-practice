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

    def freq_counter(vals):

        counts = {}

        for val in vals:
            counts[val] = counts.get(val, 0) + 1
        
        return counts

    return freq_counter(str(num1)) == freq_counter(str(num2)) 








