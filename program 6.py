
numbers = [1, -2, 0, 3, -4, 0, 5, -6]

positive = sum(map(lambda x: x > 0, numbers))
negative = sum(map(lambda x: x < 0, numbers))
zero = sum(map(lambda x: x == 0, numbers))

total = len(numbers)

print("Ratio of positive numbers:", positive / total)
print("Ratio of negative numbers:", negative / total)
print("Ratio of zeros:", zero / total)
