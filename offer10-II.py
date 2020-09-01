def numWays(n):
    # 剩1阶台阶时，前面有f(n-1)种跳法
    # 剩2阶台阶时，前面有f(n-2)种跳法
    # f(n) = f(n-1) + f(n-2) ---> 斐波那契数列
    # 但是 f(0) = 1, f(1) = 1, f(2) = 2
    dp = [0 for i in range(n+1)]
    #print(dp)
    for i in range(n+1):
        if i == 0:
            dp[i] = 1
        elif i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i-1]+dp[i-2]
    return dp[n] % 1000000007
print(numWays(7))