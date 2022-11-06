def single_letter_count(word, letter = 0):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    #count method, check membership
    # for letter in word:
    #     if letter in word.lower(): 
    #         return word.count(letter)
    #     else:
    #         return letter
    # convert the word and letter to lower, make count on letter
    return word.lower().count(letter.lower())
      
       
            

    
