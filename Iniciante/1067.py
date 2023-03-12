X = int(input())

while True:
    if X >= 1 and X <= 1000:
        for num in range(1, X+1):
            if num %2 != 0:
                print("{}".format(num))
        break
    else:
        X = int(input())