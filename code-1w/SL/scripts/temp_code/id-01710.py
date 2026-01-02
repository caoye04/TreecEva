import itertools

def analyze_readings(readings):
    """Irrelevant function: simulates sensor data analysis (unused)"""
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return [x for x in readings if x > avg], variance

def transform_sequence(seq):
    """Irrelevant transformation using itertools (partially unused)"""
    grouped = [list(g) for k, g in itertools.groupby(seq)]
    flattened = list(itertools.chain.from_iterable(grouped[::-1]))
    return [x * 2 for x in flattened if x % 2 == 0]

def decode_payload(payload_str):
    """Unused decoy function that looks important"""
    chars = [chr(int(c) + 65) for c in payload_str if c.isdigit()]
    return ''.join(chars)

def filter_and_aggregate(data_list, threshold=3.5):
    # Real computation starts here — subtle and buried
    filtered = [x for x in data_list if x >= threshold]
    base_total = sum(filtered)
    adjustment = 0
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            adjustment += val * 0.1
        else:
            adjustment -= val * 0.05
    return base_total, adjustment

def process_entries(entries_dict):
    # Mix of relevant and irrelevant operations
    values = []    
    temp_log = []  # Distractor: logs intermediate steps (not used)
    for key, nums in entries_dict.items():
        if 'temp' in key:
            temp_log.append(f"Processing {key}")
            continue  # Skip temperature-like keys (red herring)
        cleaned = [round(x, 2) for x in nums if x is not None]
        values.extend(cleaned)
    
    # Actual core data extraction
    primary_values = [v for v in values if v > 0]
    return primary_values

def calculate_final_score(dataset):
    total, adj = filter_and_aggregate(dataset, 2.8)
    score = total + adj
    bonus = 0
    
    # Bit manipulation red herring
    binary_rep = bin(int(score))[2:]
    ones_count = binary_rep.count('1')
    if ones_count > 5:
        bonus += 10
    
    # Logical check with short-circuiting distraction
    is_stable = len(binary_rep) > 4 and (ones_count / len(binary_rep)) < 0.7
    if is_stable or bonus > 5:
        bonus += 5

    # Real bonus logic (hidden in plain sight)
    magnitude = len(str(int(score)))
    if magnitude == 3:
        bonus += 7
    elif magnitude == 4:
        bonus += 12
    else:
        bonus += 3

    final = score + bonus
    
    # Irrelevant string processing using enumerate and zip
    labels = ['A', 'B', 'C', 'D', 'E']
    indexed = list(enumerate(labels))
    paired = list(zip(primary_values[:len(labels)], labels))  # primary_values undefined here!
    
    # Fix scope issue by redefining locally (distractor code)
    local_vals = [1.1, 2.2, 3.3]
    paired = list(zip(local_vals, labels))
    
    # Final meaningless transformation
    encoded = ''.join([p[1].lower() if p[0] > 2.0 else p[1].upper() for p in paired])
    
    return round(final, 3)

# --- MAIN EXECUTION ---
if __name__ == '__main__':
    # Simulated dataset — realistic domain: environmental sampling (avoiding network/sensor)
    raw_entries = {
        'sample_01': [4.2, None, 5.1, 3.8],
        'sample_02': [2.9, 3.0, 4.4, 6.1],
        'temp_aux_1': [1.1, 2.2, 3.3],  # skipped in processing
        'sample_03': [3.7, 4.9, 2.8, 5.0],
        'calib_ref': [0.5, 0.7, 0.6],     # low values, will be filtered later
        'sample_04': [4.0, 3.9, 4.3, 4.1]
    }

    # Step 1: Process entries (removes temp and Nones)
    processed_data = process_entries(raw_entries)

    # Step 2: Call the key function
    final_score = calculate_final_score(processed_data)

    # Step 3: Print result as required
    print(f"Target result: {final_score}")