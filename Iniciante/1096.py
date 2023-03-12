i = 1
j = 7


if i <= 9:
    if j >= 5:
        print("I={} J={}".format(i,j))
        j -= 1
    else:
        j = 7
        i += 2
        print("I={} J={}".format(i,j))
        j -= 1


