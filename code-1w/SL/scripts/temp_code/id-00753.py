import itertools

def analyze_sequence(data):
    # Irrelevant transformation (distractor)
    normalized = [x / max(data) for x in data]
    weighted_sum = sum(x * i for i, x in enumerate(data))
    
    # Semi-relevant filtering
    filtered = [x for x in data if x > sum(data) / len(data)]
    
    # Key computation embedded in noise
    base_value = sum(filtered) // len(filtered) if filtered else 0
    
    # Dead code path (misleading)
    if len(data) > 100:
        return -1  # Never reached
    
    return base_value


def transform_pairs(data):
    # Use of zip and enumerate (required python features)
    paired = list(zip(data, data[1:]))
    differences = [abs(a - b) for a, b in paired]
    indexed_diffs = [(i, v) for i, v in enumerate(differences) if v % 2 == 0]
    
    # Bitwise distraction
    magic_offset = 0
    for i in range(len(indexed_diffs)):
        magic_offset ^= i & 3  # Adds noise
    
    return differences


def calculate_final_score(data_chunk):
    # Accumulation with red herring variables
    temp_result = 0
    tracker = []
    
    for val in data_chunk:
        temp_result += val ** 2
        tracker.append(temp_result % 7)  # Tracked but unused later
    
    # Core logic hidden among distractions
    checksum = sum(itertools.islice(data_chunk, 0, None, 2))  # Every other element
    adjustment = len([x for x in data_chunk if x & 1])  # Count odd values
    
    final_score = temp_result - checksum + adjustment
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Main execution block
raw_input = [12, 7, 3, 19, 4, 8, 11, 5]

# Distractor preprocessing chain
shifted_data = [x + 2 for x in raw_input]
decayed = [int(x * 0.9) for x in shifted_data]  # Not actually used
processed_data = [x - 1 for x in shifted_data if x > 5]

# Secondary irrelevant computation
_ = analyze_sequence(raw_input)
_ = transform_pairs(processed_data)

# Critical execution point
final_score = calculate_final_score(processed_data)