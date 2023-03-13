
while True:
    line = input().split(" ")

    X, Y = line

    X = int(X)
    Y = int(Y)

    if X != 0 and Y != 0:
        if X > 0 and Y > 0:
            print("primeiro")
        elif X > 0 and Y < 0:
            print("quarto")
        elif X < 0 and Y < 0:
            print("terceiro")
        elif X < 0 and Y > 0:
            print("segundo")
    else:
        break
