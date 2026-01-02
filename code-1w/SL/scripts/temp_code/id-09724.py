def analyze_temperatures(raw_readings):
    adjusted = [temp + 2 for temp in raw_readings if temp < 30]
    outliers = [temp for temp in raw_readings if temp > 40]
    normalized = [round((temp - 25) / 5) for temp in raw_readings]
    return adjusted, normalized, outliers


def filter_stable_readings(normalized):
    stable = []
    for i, val in enumerate(normalized):
        if i > 0 and abs(val - normalized[i-1]) <= 1:
            stable.append(val)
    return stable


def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Simplified pseudo-entropy
    return round(entropy, 4)


def calculate_final_score(processed_data):
    base = sum(processed_data)
    bonus = len(processed_data) // 3
    penalty = 0
    
    for i, x in enumerate(processed_data):
        if i % 2 == 0 and x > 2:
            penalty += 1
    
    # Irrelevant computation block (distractor)
    temp_result = [a ^ b for a, b in zip(processed_data, processed_data[1:])]
    avg_temp = sum(temp_result) / len(temp_result) if temp_result else 0
    dummy_offset = int(avg_temp * 0.5)

    # More distraction: set operation with no impact
    unique_caps = set([x | 1 for x in processed_data])
    extra_adjustment = len(unique_caps) - len(processed_data)

    final_score = base + bonus - penalty + dummy_offset + extra_adjustment
    return final_score

# Main execution
raw_sensor_data = [22, 25, 29, 31, 36, 24, 27, 45, 33, 26]
adjusted_readings, normalized_readings, _ = analyze_temperatures(raw_sensor_data)
stable_readings = filter_stable_readings(normalized_readings)

# Additional irrelevant processing (dead-end)
windowed_sums = [sum(normalized_readings[i:i+3]) for i in range(len(normalized_readings)-2)]
smoothed = [sum(windowed_sums[j:j+2]) // 2 for j in range(len(windowed_sums)-1)]

# Key data used in answer
processed_data = [x * 2 for x in stable_readings if x != 0]

# Another distraction: slicing and reversing
reversed_slice = normalized_readings[::-1][:len(normalized_readings)//2]
shadow_value = sum(reversed_slice) // 2 if reversed_slice else 0

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")