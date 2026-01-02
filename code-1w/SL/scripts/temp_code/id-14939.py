def analyze_pattern(sequence):
    count_a = 0
    count_b = 0
    temp_sum = 0
    for i, char in enumerate(sequence):
        if i % 2 == 0:
            count_a += ord(char) % 5
        else:
            count_b += (ord(char) // 3) % 4
    return (count_a * count_b) % 100

def validate_thresholds(thresholds):
    valid_count = 0
    for t in thresholds:
        if t > 0 and t != 5:
            valid_count += 1
    return valid_count > 2

def calculate_checksum(data_points):
    checksum = 0
    for i in range(len(data_points)):
        checksum ^= data_points[i] * (i + 1)
    return checksum % 1000

def calculate_adjusted_efficiency(data_points, thresholds):
    base_efficiency = 0
    adjustment_factor = 0
    temp_data = [x for x in data_points if x > 10]
    
    # Irrelevant helper computation (distractor)
    outlier_count = sum(1 for x in data_points if x < 5)
    ignored_value = outlier_count * 17
    
    for idx, val in enumerate(temp_data):
        if val % 2 == 0:
            base_efficiency += val // 2
        else:
            base_efficiency -= -(-val // 3)  # Ceiling division
    
    # Compute adjustment using threshold pattern
    threshold_xor = 0
    for a, b in zip(thresholds[:-1], thresholds[1:]):
        threshold_xor ^= (a + b) % 8
    
    adjustment_factor = threshold_xor if validate_thresholds(thresholds) else 5
    
    # Secondary distractor: complex but unused calculation
    mirrored_pairs = [(thresholds[i], thresholds[-i-1]) for i in range(len(thresholds)//2)]
    symmetry_score = sum(x * y for x, y in mirrored_pairs) % 50
    
    # Final efficiency combines base and adjustment
    raw_result = base_efficiency + adjustment_factor * 3
    
    # Extra red herring: character counting in magic string
    magic_tag = "efficiency_boost_2x"
    extra_bonus = sum(1 for c in magic_tag if c in 'aeiou') * 2
    
    final_score = raw_result + extra_bonus  # This line sets final_score
    
    return final_score

# Main execution
sequence_input = "abcdeffeedd"
data_points = [12, 15, 3, 22, 8, 19, 4, 27]
thresholds = [6, 12, 9, 4, 11]

pattern_code = analyze_pattern(sequence_input)
checksum = calculate_checksum(data_points)

# Key statement
final_score = calculate_adjusted_efficiency(data_points, thresholds)

print(f"Result: {final_score}")