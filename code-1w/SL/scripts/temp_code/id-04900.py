def analyze_frequency(seq, threshold):
    count = 0
    for freq in seq:
        if freq > threshold:
            count += 1
    return count

# Irrelevant helper function (dead code path)
def decrypt_key(token):
    base = 0
    for c in token:
        base ^= ord(c)
    return base * 7 % 13

def build_lookup(keys):
    lookup = {}
    for i, key in enumerate(keys):
        lookup[key] = i * i + 2  # Distractor computation
    return lookup

def merge_sequences(primary, secondary, offset=3):
    result = []
    for a, b in zip(primary, secondary):
        result.append(a + b - offset)
    return result

def filter_noisy_entries(data_list, noise_level=0.5):
    clean_data = []
    total = 0
    for item in data_list:
        if abs(item) > noise_level:
            clean_data.append(item)
            total += item * 0.1
    return clean_data  # 'total' is unused (misleading intermediate)

def transform_coordinates(x_vals, y_vals):
    coords = []
    for i, (x, y) in enumerate(zip(x_vals, y_vals)):
        adjusted = (x * 2 + i, y - i * 0.5)
        coords.append(adjusted)
    return coords

def calculate_entropy(values):
    entropy = 0.0
    norm = sum(v ** 2 for v in values)
    for v in values:
        prob = (v ** 2) / norm if norm else 0
        if prob > 0:
            entropy -= prob * __import__('math').log(prob)
    return entropy * 100

def process_transmission(chain, config):
    # Core logic starts here
    temp = []
    multiplier = config['gain']
    shift = config.get('shift', 0)
    
    for i, val in enumerate(chain):
        if i % 2 == 0:
            temp.append(val * multiplier)
        else:
            temp.append(val + shift)
    
    # Secondary transformation
    staged = []
    for j, x in enumerate(temp):
        if j < len(temp) // 2:
            staged.append(x + 5)
        else:
            staged.append(x * 2)
    
    # Final aggregation with reduction
    accumulator = 0
    for idx, num in enumerate(staged):
        if idx % 3 == 0:
            accumulator += num
        elif idx % 4 == 0:
            accumulator -= num  # Overlap at idx=0 handled correctly
    
    return int(accumulator)

# Main execution block
if __name__ == "__main__":
    # Input data
    signal_chain = [3, -1, 4, 1, 5, 9, 2, 6]
    keys = ['A', 'B', 'C', 'D']
    x_points = [1, 2, 3, 4]
    y_points = [10, 20, 30, 40]
    raw_seq = [0.1, 0.8, 0.3, 1.2, 0.9]
    secondary_seq = [2, 1, 3, 0, 4]

    # Distractor variables (irrelevant)
    key_token = "XyZ9"
    decryption_result = decrypt_key(key_token)
    lookup_table = build_lookup(keys)
    coordinate_map = transform_coordinates(x_points, y_points)
    frequency_analysis = analyze_frequency(raw_seq, 0.5)
    merged_stream = merge_sequences(raw_seq, secondary_seq)
    filtered_data = filter_noisy_entries(merged_stream, 0.3)
    entropy_score = calculate_entropy(signal_chain)

    # Configuration map (used)
    config_map = {
        'gain': 3,
        'shift': -2
    }

    # Critical statement
    final_signal = process_transmission(signal_chain, config_map)
    
    print(f"Result: {final_signal}")