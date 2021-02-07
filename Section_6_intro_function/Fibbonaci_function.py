def fibbonaci(n: int) -> int:
    """

    :param n: enter the value till which you want the fibbonnaci number
    :return: returns the fibbonaci number
    """
    if 0<= n <= 1:
        return n
    nminus1, nminus2 = 1, 0
    results = None
    for i in range(n-1):
        results = nminus1 + nminus2
        nminus2 = nminus1
        nminus1 = results

    return results
for i in range(36):
    print(i + 1, fibbonaci(i))