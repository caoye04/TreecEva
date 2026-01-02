def analyze_temperatures(temp_readings):
    adjusted = []
    outlier_count = 0
    base_offset = 273.15
    for i, temp in enumerate(temp_readings):
        if temp < -50 or temp > 50:
            outlier_count += 1
            continue
        kelvin = temp + base_offset
        adjusted.append(kelvin)
    
    # Distractor: unused computation
    avg_kelvin = sum(adjusted) / len(adjusted) if adjusted else 0
    normalized = [round(x / avg_kelvin * 100) for x in adjusted] if avg_kelvin != 0 else []

    return adjusted, outlier_count


def filter_stable_ranges(temps):
    stable_segments = []
    current_segment = []
    for temp in temps:
        if 290 <= temp <= 310:
            current_segment.append(temp)
        else:
            if len(current_segment) >= 3:
                stable_segments.append(current_segment[:])
            current_segment.clear()
    if len(current_segment) >= 3:
        stable_segments.append(current_segment)
    return stable_segments


def calculate_mod_scores(values):
    mod_sum = 0
    for v in values:
        mod_sum += v % 17
    # Semi-relevant distractor
    adjustment_factor = len(values) % 5 if values else 0
    return mod_sum + adjustment_factor


def calculate_final_score(data_list):
    score_components = []
    for idx, segment in enumerate(data_list):
        raw_sum = sum(segment)
        length_bonus = len(segment) * 3
        mod_score = calculate_mod_scores(segment)
        total_segment = raw_sum + length_bonus + mod_score
        score_components.append(total_segment)
    
    # Final aggregation
    final_score = sum(score_components) // len(score_components) if score_components else 0
    
    # Irrelevant transformation
    inverted_scores = [1000 // (x + 1) for x in score_components]
    
    return final_score

# Main execution
raw_temps = [25, -60, 30, 32, 33, 45, 10, 15, 20, 28, 31, 34, 36, -70, 18]
processed_temps, _ = analyze_temperatures(raw_temps)
stable_ranges = filter_stable_ranges(processed_temps)

# Unused but plausible intermediate
all_pairs = list(zip(processed_temps[:-1], processed_temps[1:]))
consecutive_diffs = [round(b - a, 2) for a, b in all_pairs]

# Key statement
final_score = calculate_final_score(stable_ranges)
print(f"Target result: {final_score}")