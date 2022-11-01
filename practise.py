squares = []

for count in range(1, 6, 1):
    squares.insert(count - 1, count ** 3)

print(squares)

squares_2nd = [ value ** 3 for value in range(1, 6, 1) ]

print(squares_2nd)