from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    temp_sum = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] ^ sequence[j]) & 1:  # XOR and check least significant bit
                count += 1
            temp_sum += abs(sequence[i] - sequence[j])
    return count

def preprocess_input(raw):
    cleaned = [x for x in raw if x % 2 == 1]  # Keep only odd numbers
    shifted = [(x << 1) for x in cleaned]     # Left shift by 1
    return [x % 17 for x in shifted]          # Modulo to bound values

def calculate_final_score(data):
    base = sum(data)
    bonus = 0
    indices = [i for i, x in enumerate(data) if x > 5]
    pairs = list(combinations(indices, 2))
    if len(pairs) > 3:
        bonus = len(pairs) // 2
    
    # Distractor: irrelevant string processing
    status_log = "Processing complete"
    log_upper = status_log.upper()
    log_chars = len(log_upper)
    dummy_result = ''.join([c for c in log_upper if c in 'AEIOU'])
    
    # More distractors: unused computations
    magnitude = 0
    for k in range(1, 8):
        magnitude += pow(k, 2) % 4
    
    adjustment = 0
    for idx, val in enumerate(data):
        if idx % 3 == 0 and val % 2 == 0:
            adjustment -= val
        elif idx % 4 == 0 and val % 3 == 0:
            adjustment += val // 3
    
    final_score = base + bonus + adjustment
    return final_score

# Main execution
raw_input = [12, 7, 3, 8, 5, 9, 4, 6]
filtered_data = preprocess_input(raw_input)
processed_data = []
for index, value in enumerate(filtered_data):
    transformed = value * 2 + (index & 3)
    processed_data.append(transformed)

# Additional red herring: unused data structure
reversed_pairs = list(zip(filtered_data[::-1], range(len(filtered_data))))
size_check = len(reversed_pairs) * 2

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")