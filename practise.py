squares = []
for value in range(1, 6):
    square = value ** 3
    squares.append(square)

print(squares)

for count in range(1, 6):
    squares.insert(count - 1, count ** 3)

print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))
