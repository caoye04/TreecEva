values = [15, 22, 8, 35, 12]
targets = [22, 8, 35, 12, 15]
matched_sum = 0

for i, (x, y) in enumerate(zip(values, targets)):
    if x == y:
        matched_sum += x

print(f"Result: {matched_sum}")