def calculateSumOfNumbersInString(inputString: str) -> int:
    temp = ""
    sum = 0
    for i in range(0, len(inputString)):
        ch = inputString[i]
        if ch.isdigit():
            temp += ch
        else:
            sum += int(temp)

    return sum + int(temp)
