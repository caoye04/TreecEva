from itertools import combinations

def analyze_patterns(data):
    # Distractor: Analyze character frequency (not directly used)
    freq = {}
    for item in data:
        for c in str(item):
            freq[c] = freq.get(c, 0) + 1
    
    # Semi-relevant: Count digit transitions
    transitions = 0
    for i in range(len(data) - 1):
        last_digit = str(data[i])[-1]
        first_next = str(data[i+1])[0]
        if last_digit.isdigit() and first_next.isdigit():
            transitions += abs(int(last_digit) - int(first_next))
    
    return transitions  # Not used in final result

def compute_total(values, mods):
    adjusted = []
    for i, val in enumerate(values):
        mod_factor = mods[i % len(mods)]
        temp_val = val * (mod_factor + 1)
        adjusted.append(temp_val)
    
    # Use conditional expression to filter noise
    cleaned = [x for x in adjusted if x > sum(adjusted) / len(adjusted)]
    
    # Real computation: sum of squares of top half
    sorted_vals = sorted(cleaned, reverse=True)
    midpoint = len(sorted_vals) // 2
    top_half_squares = [v ** 2 for v in sorted_vals[:midpoint]]
    
    return sum(top_half_squares)

def main():
    # Input data
    base_values = [12, 7, 19, 4, 8, 15]
    modifiers = [2, -1, 3]

    # Irrelevant pre-processing
    encoded = []
    for idx, (char, num) in enumerate(zip('ABCDEF', base_values)):
        shift = idx * 2
        encoded.append(f'{char}{num + shift}')
    
    # Dead-end combinatorics
    pairs = list(combinations(base_values, 2))
    large_pairs = [p for p in pairs if (p[0] + p[1]) > 20]
    pair_count = len(large_pairs)

    # Unused state tracking
    history = []
    temp_sum = 0
    for v in base_values:
        temp_sum += v
        if temp_sum > 25:
            history.append(temp_sum)
            temp_sum = 0
    
    # Key statement
    final_score = compute_total(base_values, modifiers)
    
    # Print result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()