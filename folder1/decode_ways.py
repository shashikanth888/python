def numDecodings(s):
    if not s:
        return 0
    
    dp = [0 for _ in range(len(s) + 1)]
    dp[0]=1
    dp[1] = 0 if s[0] == '0' else 1
    
    for i in range(2, len(dp)):
        print(dp)
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if int(s[i-2:i]) <= 26 and int(s[i-2:i]) >= 10:
            dp[i] += dp[i-2]
    return dp[len(s)]

numDecodings("1213121")