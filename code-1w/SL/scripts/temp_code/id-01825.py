from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing with red herrings
def preprocess_readings(raw):    
    # Irrelevant transformation (distractor)
    inverted = [max(raw) - x for x in raw]
    shifted = [x - 1 for x in raw if x > 5]  # Partial filter, unused later
    normalized = [round(x / sum(raw), 3) for x in raw]
    return normalized

# Misleading analysis branch (dead path)
def deprecated_analysis(seq):
    histogram = defaultdict(int)
    for x in seq:
        histogram[round(math.log(abs(x) + 1))] += 1
    return dict(histogram)

# Core transformation function (used)
def transform_sequence(seq, mode='advanced'):
    result = []
    cumulative = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            cumulative += val ** 2
        else:
            cumulative -= val
        result.append(cumulative)
    # Slicing operation (relevant)
    return result[::-1]  # Reverse the transformed sequence

# Secondary helper with decoy logic
def compute_tendency(data):
    if len(data) == 0:
        return 0
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    # Following line looks important but is not used in final result
    adjusted = [x * (1 + 0.1 * math.sin(i)) for i, x in enumerate(data)]
    return avg  # Only average is returned and used

# Main pattern analyzer (critical path)
def analyze_pattern(series, limit):
    count_tracker = Counter()
    temp_flags = []
    
    for idx, item in enumerate(series):
        if item > limit:
            count_tracker['high'] += 1
            temp_flags.append(1)
        elif item < -limit:
            count_tracker['low'] += 1
            temp_flags.append(-1)
        else:
            temp_flags.append(0)
    
    # Complex conditional branching (3 levels deep)
    adjustment = 0
    if count_tracker['high'] > 0:
        if count_tracker['low'] == 0:
            if count_tracker['high'] % 3 == 0:
                adjustment = 5
            else:
                adjustment = -3
        else:
            adjustment = (count_tracker['high'] - count_tracker['low']) * 2
    else:
        adjustment = -1
    
    # Final computation using bit manipulation (red herring XOR chain)
    signature = 0
    for f in temp_flags[-5:]:  # Only last 5 matter, but others computed
        signature ^= (f * 7 + idx) & 15  # Bitwise distraction
    
    # Actual answer derivation (non-obvious)
    base_score = sum(series[:len(series)//2])  # First half sum
    modifier = int(compute_tendency(temp_flags))  # Uses tendency of flags
    final_value = base_score + modifier + adjustment
    
    return final_value

# --- Execution Block ---
if __name__ == '__main__':
    # Initial dataset
    raw_sensor_data = [3, 7, 2, 8, 4, 6]
    
    # Distractor: unused processed variants
    processed_A = preprocess_readings(raw_sensor_data)
    trend_snapshot = deprecated_analysis(raw_sensor_data)  # Dead call
    
    # Key transformation
    transformed_data = transform_sequence(raw_sensor_data)
    
    # Multiple variable assignments (some irrelevant)
    threshold = 10
    floor_limit = 2
    ceiling_override = 15  # Unused
    debug_mode = False  # Unused flag
    
    # Critical execution point
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")