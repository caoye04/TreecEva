import itertools

genetic_markers = [12, 28, 45, 63, 79]
marker_pairs = list(itertools.combinations(genetic_markers, 2))
encoded_differences = {abs(a ^ b) for a, b in marker_pairs}
filtered_codes = {code for code in encoded_differences if bin(code).count('1') > 3}
uniqueness_score = sum(filtered_codes) % 1000
print(f"Result: {uniqueness_score}")