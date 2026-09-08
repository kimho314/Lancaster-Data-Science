# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

list = []
def fib(n):
    for i in range(n+1):
        if i == 0:
            list.append(0)
        elif i == 1:
            list.append(1)
        else:
            res = list[i-1] + list[i-2]
            list.append(res)
    return list[n]

print(fib(10))
print(fib(1000))