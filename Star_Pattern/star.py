rows = int(input("Enter Star Pattern Rows = "))

print("Star pattern")

for i in range(rows, 0, -1):
    for j in range(1, i):
        print(' ', end='')
    for k in range(0, rows):
        print('*', end='')
    print()