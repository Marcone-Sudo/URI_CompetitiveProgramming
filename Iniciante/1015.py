line1 = input().split(" ")
line2 = input().split(" ")

x1, y1 = line1
x2, y2 = line2

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

print("{:.4f}".format((((x2-x1)**2) + ((y2-y1))**2)**0.5))