def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Distractor: Analyze trend but not used later
    increasing_runs = 0
    for t in trend:
        if t == 1:
            increasing_runs += 1

    # Irrelevant string processing (distractor)
    status_log = "Analysis complete"
    log_upper = status_log.upper().replace(" ", "_")
    checksum = sum(ord(c) for c in log_upper) % 100

    return [x * 2 for x in sequence if x % 2 == 1]  # Returns doubled odd values


def transform_dataset(data, threshold=10):
    modified = []
    temp_sum = 0
    
    for val in data:
        if val < 0:
            adjusted = abs(val) ** 0.5
        else:
            adjusted = val ** 0.5 if val > 0 else 0
        
        normalized = round(adjusted, 2)
        modified.append(normalized)
        
        # Dead computation branch (distractor)
        if normalized > 5:
            temp_sum += normalized * 0.1  # Not actually used
    
    # List comprehension with filtering (relevant)
    filtered = [x for x in modified if x >= 1.0]
    
    # Extra function inside (misleading complexity)
    def get_stats(lst):
        return {
            'min': min(lst),
            'max': max(lst),
            'avg': sum(lst) / len(lst)
        }
    
    stats = get_stats(filtered)
    scaling_factor = int(stats['avg']) if stats['avg'] > 2 else 1
    
    return [x * scaling_factor for x in filtered]


def calculate_final_score(payload):
    base = sum(payload)
    penalty = 0
    
    # Bitwise manipulation (moderately relevant)
    for val in payload:
        if val > 4:
            penalty ^= int(val) & 3  # XOR with lower 2 bits
    
    # Conditional expression chain
    multiplier = 2 if len(payload) > 5 else (1.5 if base > 10 else 1)
    
    # Final score computation
    final_score = (base * multiplier) - penalty
    
    # Red herring: unused transformation
    inverted = list(map(lambda x: 1/(x+1), payload))
    avg_inverse = sum(inverted) / len(inverted)
    
    return int(final_score)

# Main execution flow
raw_sequence = [3, -4, 5, 2, 8, -1, 6]
data_a = [x**2 - 4 for x in raw_sequence if x != -1]
processed_data = transform_dataset(analyze_pattern(data_a))

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")