def calculate_final_score(points, factor):
    base = points % 7
    adjustment = (base ** 2) - 3 if base > 3 else (base * 2) + 1
    
    # Irrelevant computation (distractor)
    temp_debug = [i * i for i in range(5)]
    avg_debug = sum(temp_debug) / len(temp_debug)
    
    multiplier = 1.5 if points > 50 else 1.0
    scaled = points * multiplier
    
    # Another semi-relevant but non-critical path
    if factor > 0:
        scaled -= (factor * 2) % 9
    
    # Core logic contribution
    offset = 5 if scaled % 2 == 0 else -2
    preliminary = scaled + adjustment + offset
    
    # Dead code (not used) - red herring
    unused_trace = {'step1': base, 'step2': adjustment, 'ignored': True}
    
    # Final calculation involving modular arithmetic and conditional logic
    final = int(preliminary // 1.2)
    return final

# Main execution
raw_points = 87
penalty_factor = 4
auxiliary_weight = 0.75  # Unused in final result

# Simulate intermediate logging (irrelevant to output)
log_entries = []
for i in range(3):
    log_entries.append(f"Processing stage {i + 1}")

# Key statement
final_score = calculate_final_score(raw_points, penalty_factor)

# Print result as required
print(f"Target result: {final_score}")