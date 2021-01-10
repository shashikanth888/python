def reverseAlphabetCharsOnly(inputString: str) -> str:
    inputChar = list(inputString)
    right = len(inputString) - 1
    left = 0
    while left < right:
        if not inputChar[left].isalpha():
            left = left + 1
        elif not inputChar[right].isalpha():
            right = right - 1
        else:
            temp = inputChar[left]
            inputChar[left] = inputChar[right]
            inputChar[right] = temp
            left = left + 1
            right = right - 1
    return ''.join(inputChar)
