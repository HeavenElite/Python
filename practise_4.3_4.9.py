sequence = []

for number in range(1, 1_000_001):
    sequence.append(number - 0.1)

print(max(sequence), min(sequence), sum(sequence))

odds = [ value for value in range(1, 20, 2) ]

for odd in odds:
    print(odd)

for number in [ value ** 3 for value in range(1,11) ]:
    print(number)

