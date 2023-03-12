line = input().split(" ")

codigo, quantidade = line

codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    print("Total: R$ {:.2f}".format(quantidade*4.00))
elif codigo == 2:
    print("Total: R$ {:.2f}".format(quantidade*4.50))
elif codigo == 3:
    print("Total: R$ {:.2f}".format(quantidade*5.00))
elif codigo == 4:
    print("Total: R$ {:.2f}".format(quantidade*2.00))
elif codigo == 5:
    print("Total: R$ {:.2f}".format(quantidade*1.50))