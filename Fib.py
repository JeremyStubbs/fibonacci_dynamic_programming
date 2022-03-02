# Fibonacci Memoization
def fib (n, answers = {}):
    if (n in answers):
        return answers[n]
    if (n<=2):
        return 1
    answers[n]=fib(n-1, answers)+fib(n-2, answers)
    # print(n, answers)
    return answers[n]
    

# print(fib(200))

# Fibonacci Tabulation
def fib(n):
    table = [0]*(n+2)
    table[1] = 1
    for i in range(n):
        table[i+1] += table[i]
        table[i+2] += table[i]
    print(table)
    return table[n]


print(fib(20))

# Grid Traveler Tabulation
