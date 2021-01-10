def checkPairSumExists(rows: int, cols: int, arr: List[List[int]], sum: int) -> bool:
    localSet = set()
    for i in range(0, rows):
        for j in range(0, cols):
            if sum - arr[i][j] in localSet:
                return True
            else:
                localSet.add(arr[i][j])
    return False
