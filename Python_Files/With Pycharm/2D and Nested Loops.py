numbers = [
    [1, 6, 7, 8],
    [5, 9, 4, 1],
    [2, 3, 10, 21],
    [24, 45, 87],
    [65, 89],
    [78]
]
print(numbers)
print(numbers[0])
print(type(numbers))
print(numbers[3][1])
print("DONE")

for row in numbers:
    print(row)
print("NEXT")

for col in numbers:
    print(col)
    for row in col:
        print("row")
print("END")

for row in numbers:
    for col in row:
        print(col)
        print(row)

print("AGAIN!!!")
