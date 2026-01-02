from itertools import combinations

def analyze_sequence(data):
    # Extract subsequences using slicing
    n = len(data)
    subsequences = [data[i:j] for i in range(n) for j in range(i+2, min(i+5, n))]
    
    # Irrelevant transformation (distractor)
    amplified = [x * 1.5 + 2 for x in data]
    amplified_sum = sum(amplified)

    # Character frequency counting (semi-relevant)
    char_count = {}
    for val in data:
        c = str(val)[-1]  # last digit as character
        char_count[c] = char_count.get(c, 0) + 1
    
    # Generate pairs for correlation check (not used later)
    pair_sums = [a + b for a, b in combinations(data, 2) if a > b]

    # Actual relevant processing: filter and transform
    filtered = [x for x in data if x % 3 == 0]
    normalized = [x / max(filtered) for x in filtered]
    smoothed = [sum(normalized[max(0,i-1):i+2]) / (3 if i not in (0, len(normalized)-1) else 2) for i in range(len(normalized))]
    
    return smoothed

def calculate_optimal_yield(seq):
    base = sum(seq)
    adjustment = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            adjustment += val * 0.1
        else:
            adjustment -= val * 0.05
    
    # Dummy loop with no effect (dead code path)
    temp_result = 0
    for _ in range(3):
        temp_result += 10
        temp_result -= 10  # cancels out

    return int(base * (1 + adjustment))

# Main execution
raw_input = [9, 12, 15, 18, 21, 24, 30]
data_stats = {"count": len(raw_input), "peak": max(raw_input), "baseline": sum(raw_input) / len(raw_input)}

# Preprocessing step with slicing
trimmed = raw_input[1:-1]  # remove first and last
extended = trimmed + [trimmed[-1] + 3, trimmed[-1] + 6]
sorted_extended = sorted(extended, reverse=True)

# Secondary irrelevant sort
sorted_by_digit = sorted(extended, key=lambda x: str(x)[-1])

# Actual processing pipeline
processed_data = analyze_sequence(sorted_extended)
intermediate_total = sum(processed_data) * 100  # red herring variable

# Key statement
final_yield = calculate_optimal_yield(processed_data)

print(f"Result: {final_yield}")