n = int(input())

five, mod = divmod(n, 5)

if mod % 2:
    five -= 1
    two = (mod + 5) // 2
    print(five + two)
else:
    two = mod // 2
    print(five + two)