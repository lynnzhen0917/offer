#斐波那契数列
#method 1: 递归，大量计算
# def fib1(n):
#     if n <= 1:
#         return n
#     return fib1(n-1)+fib1(n-2)

#method2: 动态规划-->O(n) O(1)
# def fib2(n):
#     a,b = 0,1
#     for i in range(n):
#         a,b = b,a+b
#     return a % 1000000007
def fib3(n):
    dp = [0 for i in range(n+1)]
    #print(dp)
    for i in range(n+1):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i-1]+dp[i-2]
    return dp[n] % 1000000007
