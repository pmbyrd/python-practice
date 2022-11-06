def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    #TL to BR is x,y next row is x+1, y+1  ** a primary line goes foward
    # BL to TR is -x,-y, next row x,y a secondary line goes backwards
    # get the num at it's position and add it to the sum
    # intialize a sum and loop over the values in the matrix by position

    sum = 0

    for num in range(len(matrix)):
        sum += matrix[num][num]
        sum += matrix[num][-1 -num]
    
    return sum
