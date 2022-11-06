def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #loop over the phrase if char is to_swap that char is swapped, use swapcase()

    to_swap = to_swap.lower()

    swapped_phrase = ""

    for char in phrase:
        if char.lower() == to_swap:
            char = char.swapcase() 
        swapped_phrase += char
    return swapped_phrase
