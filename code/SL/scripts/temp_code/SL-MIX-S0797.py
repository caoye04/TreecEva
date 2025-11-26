def count_valid_permutations(n):
    values = [i for i in range(1, n+1)]
    pairs = [(x, y) for x in values for y in values if x != y]
    filtered_pairs = [(a, b) for a, b in pairs if (a + b) % 3 == 0 and (a * b) > 8]
    temp_check = len([p for p in filtered_pairs if p[0] < p[1]])
    final_count = len(filtered_pairs)
    print(f"Result: {final_count}")

count_valid_permutations(6)