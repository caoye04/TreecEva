from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 7:
                count += 1
    return count

def preprocess_items(raw_list):
    filtered = [x for x in raw_list if x % 3 != 0]
    shifted = [(x * 2) % 10 for x in filtered]
    temp_analysis = sum([1 for x in shifted if x > 5])  # distractor
    return shifted

def compute_final_score(data):
    base = sum(data)
    bonus = 0
    pairs = list(combinations(data, 2))
    for p in pairs:
        if (p[0] + p[1]) % 4 == 0:
            bonus += 1
    adjustment = len(data) // 2
    final = base + bonus - adjustment
    return final

# Main execution
raw_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mask_value = 999  # irrelevant
interim_result = analyze_pattern(raw_input)  # used only for distraction
processed_data = preprocess_items(raw_input)

# Extraneous computation block (distractor)
duplicate_check = {}
for item in processed_data:
    if item in duplicate_check:
        duplicate_check[item] += 1
    else:
        duplicate_check[item] = 1
ignored_sum = sum(duplicate_check.values())  # dead use

# Key statement
final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")