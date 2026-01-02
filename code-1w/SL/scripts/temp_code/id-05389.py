def analyze_pattern(sequence):
    count = 0
    temp_sum = 0
    for char in sequence:
        if char.isdigit():
            temp_sum += int(char)
            count += 1
    average_digit = temp_sum / count if count > 0 else 0
    return temp_sum, average_digit

sequence = 'a3b7c1d4e9f2'

# Irrelevant transformation (distractor)
reversed_sequence = sequence[::-1]
doubled_values = [2 * int(c) for c in sequence if c.isdigit()]

# Relevant processing
raw_total, digit_avg = analyze_pattern(sequence)

# Simulate data normalization (mixed relevance)
normalized_total = raw_total * 1.5
offset_correction = len(sequence) // 2
adjusted_total = normalized_total - offset_correction

# Additional distractor: string analysis with no impact
vowel_count = sum(1 for c in sequence if c in 'aeiou')
letter_stats = {c: sequence.count(c) for c in set(sequence) if c.isalpha()}

# Conditional logic affecting final result
if digit_avg > 3.5:
    adjustment_factor = 3
else:
    adjustment_factor = 7

interim_score = adjusted_total * adjustment_factor

# Secondary processing chain (partially redundant)
def process_data(score, seq):
    base = score % 100
    multiplier = len([c for c in seq if c in 'abc'])
    # Dead computation (distractor)
    squared_chain = [i**2 for i in range(multiplier)]
    return base * multiplier

processed_data = process_data(interim_score, sequence)

# Final calculation
penalty = 0
for i, c in enumerate(sequence):
    if i % 3 == 0 and c.isalpha():
        penalty += 1

final_score = processed_data - penalty

# Output target result
print(f"Result: {final_score}")