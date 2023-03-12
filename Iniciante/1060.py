positivos = 0
n_ = 0

while True:
    num = float(input())
    if num != 0:
        n_ += 1
        if num > 0:
            positivos += 1
    
    if n_ == 6:
        break

print("{} valores positivos".format(positivos))


    

