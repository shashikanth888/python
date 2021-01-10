def compareProduct(num: int) -> bool:
    if num < 10:
        return False
    oddProdValue = 1
    evenProdValue = 1
    while num > 0:
        digit = num % 10
        oddProdValue *= digit
        num = num // 10
        if num == 0:
            break
        digit = num % 10
        evenProdValue *= digit
        num = num // 10

    if evenProdValue == oddProdValue:
        return True
    return False
