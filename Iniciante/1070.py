X = int(input())
cont = 0

while True:
    
    if cont != 6:
        if X%2 != 0:
            cont += 1
            print("{}".format(X))
            X += 1

        else:
            X += 1
    else:
        break


