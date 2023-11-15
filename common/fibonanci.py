
fib = [0, 1]


def fibonanci(limit):
    if limit >= 1:
        for _ in range(2, limit):
            next_fib = fib[-1]+fib[-2]
            fib.append(next_fib)
        return fib


print(fibonanci(10))  # fibonancie series of n items

# if you want nth fibonanci number then
print(fib[-1])
