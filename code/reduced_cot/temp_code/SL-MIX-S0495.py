sequence_a = [2, 4, 6, 8, 10, 12, 14]
sequence_b = [2, 3, 6, 9, 10, 12, 16]
temp_count = 0
for item in sequence_a:
    temp_count += 1
total_matches = sum(1 for i, (a, b) in enumerate(zip(sequence_a, sequence_b)) if a == b and i % 2 == 0)
print(f"Result: {total_matches}")