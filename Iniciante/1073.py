N = int(input())

for n in range(1,N+1):
    if n % 2 == 0:
        print("{}^{} = {}".format(n,2,n**2))
