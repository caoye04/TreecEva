def analyze_pattern(sequence):
    # Irrelevant transformation: counts vowels in string representation
    str_seq = ''.join(map(str, sequence))
    vowel_count = sum(1 for c in str_seq if c.lower() in 'aeiou')

    # Distractor: unused statistical measures
    mean_val = sum(sequence) / len(sequence) if sequence else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in sequence) / len(sequence) if sequence else 0

    # Red herring function defined but not used
    def deprecated_filter(data):
        return [d for d in data if d % 2 == 0]

    # Real logic begins: find max consecutive even numbers
    max_streak = 0
    current_streak = 0
    for num in sequence:
        if num % 2 == 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    # Another distraction: string processing with no impact
    labels = ['A', 'B', 'C', 'D', 'E']
    labeled_data = list(zip(labels, sequence[:5]))
    label_sum = sum(ord(pair[0]) for pair in labeled_data)

    # Bit manipulation decoy
    bit_noise = 0
    for i, val in enumerate(sequence):
        bit_noise ^= (val << 1) | (i & 1)

    return max_streak


def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * log2(p) for p in probabilities)
    return round(entropy, 6)

# Unused recursive Fibonacci helper (dead code path)
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

# Main data pipeline
raw_input = [12, 4, 6, 7, 8, 10, 12, 14, 3, 5, 16, 18, 20]

# Step 1: Filter multiples of 3 (distractor - not used in final result)
multiples_of_three = [x for x in raw_input if x % 3 == 0]
avg_triples = sum(multiples_of_three) / len(multiples_of_three) if multiples_of_three else 0

# Step 2: Generate shifted pairs using enumerate and zip (required feature)
shifted = raw_input[1:]
enumerated_pairs = list(enumerate(zip(raw_input, shifted)))
weighted_sum = 0
for i, (a, b) in enumerated_pairs:
    weighted_sum += (b - a) * (i + 1)

# Step 3: Apply pattern analysis (actual contributor to final score)
streak_length = analyze_pattern(raw_input)

# Step 4: Compute entropy of squared residuals (red herring computation)
squared_residuals = [(x - 10) ** 2 for x in raw_input]
entropy_value = compute_entropy(squared_residuals)

# Step 5: String-based encoding distraction
data_tag = "TRACE-921"
digit_sum = sum(int(d) for d in data_tag if d.isdigit())

# Step 6: Actual core logic – average of all even numbers above 5
relevant_evens = [x for x in raw_input if x % 2 == 0 and x > 5]
core_average = sum(relevant_evens) // len(relevant_evens)  # integer division

# Step 7: Combine streak and average with weighting
preliminary_score = streak_length * 10 + core_average

# Step 8: Final aggregation with irrelevant offset
irrelevant_offset = len([x for x in raw_input if x < 0])  # always 0
final_score = preliminary_score - irrelevant_offset

print(f"Result: {final_score}")