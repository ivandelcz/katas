def to_roman(number):

    conversion_table = [
        [1000, 'M'],
        [900, 'DM'],
        [500, 'D'],
        [400, 'CD'],
        [100, 'C'],
        [90, 'XC'],
        [50, 'L'],
        [40, 'LX'],
        [10, 'X'],
        [9, 'IX'],
        [5, 'V'],
        [4, 'IV'],
        [1, 'I']
    ]

    result = ''

    for equivalent in conversion_table:
        while number >= equivalent[0]:
            result = result + equivalent[1]
            number -= equivalent[0]

    return result
