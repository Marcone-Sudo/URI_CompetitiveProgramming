n = int(input())

while True:
    if 2 < n < 1000:
        for i in range(1,11):
            print("{} x {} = {}".format(i, n, i*n))
        break