def count_multiples(a, b, c):

    # max
    largest = a
    if b > largest:
        largest = b


    max = largest

    # min
    smallest = a
    if b < smallest:
        smallest = b


    min = smallest

    # first
    if min % c == 0:
        first = min
    else:
        first = min + (c - (min % c))
    

    if first > max:
        return 0
    
    # max
    if max % c == 0:
        last = max
    else:
        last = max - (max % c)


    # count
    return (last - first) // c + 1


print(count_multiples(5,100,2))
