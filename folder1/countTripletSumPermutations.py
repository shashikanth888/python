def countTripletSumPermutations(size, arr, tripletSum) -> int:
    count = 0
    for i in range(0, size - 2):
        if tripletSum % arr[i] == 0:
            for j in range(i+1, size - 1):
                if tripletSum % (arr[i] * arr[j]) == 0:
                    value = tripletSum / (arr[i] * arr[j])
                    for k in range(j + 1, size):
                        if arr[k] == value:
                            count += 1
    return count