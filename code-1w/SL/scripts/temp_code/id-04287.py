def analyze_pattern(sequence):
    count = 0
    temp_sum = 0
    for char in sequence:
        if char.isdigit():
            temp_sum += int(char)
            count += 1
    return temp_sum // count if count else 0


def validate_entry(record):
    if len(record) < 5:
        return False
    if not record[0].isupper():
        return False
    if record.endswith('X'):
        return False
    return True


def compute_hash(key_str):
    h = 0
    for c in key_str:
        h = (h * 31 + ord(c)) % 10007
    return h


def process_metrics(data, thresholds):
    raw_values = []
    outliers = []
    correction_factor = 0.9
    
    for item in data:
        entry = item['value']
        tag = item['tag']
        
        # Irrelevant validation (distractor)
        if not validate_entry(tag):
            continue
            
        # Extract digits from tag (semi-relevant)
        digit_str = ''.join([c for c in tag if c.isdigit()])
        if digit_str:
            offset = int(digit_str) % 10
        else:
            offset = analyze_pattern(tag) % 10
        
        # Core computation
        base = entry * 1.1 + offset
        
        # Hash-based adjustment (irrelevant but looks important)
        hash_val = compute_hash(tag)
        adjustment = (hash_val % 3) - 1  # -1, 0, or 1
        adjusted = base + adjustment
        
        # Actual logic path
        if adjusted > thresholds['high']:
            outliers.append(adjusted)
        elif adjusted < thresholds['low']:
            outliers.append(adjusted)
        else:
            raw_values.append(round(adjusted * correction_factor))
    
    # Secondary filtering (some dead code here)
    filtered = []
    temp_total = 0
    for v in raw_values:
        if v == 0:
            continue  # skip zero values
        filtered.append(v)
        temp_total += v
    
    final_score = sum(filtered) // len(filtered) if filtered else 0
    
    # Red herring computation
    _ = [x ** 2 for x in outliers if x > 100]
    
    return final_score

# Main execution
if __name__ == '__main__':
    data = [
        {'value': 42, 'tag': 'Alpha1'},
        {'value': 38, 'tag': 'Beta2'},
        {'value': 46, 'tag': 'Gamma3'},
        {'value': 35, 'tag': 'Delta'},
        {'value': 51, 'tag': 'Epsilon5'},
        {'value': 20, 'tag': 'Zeta9'}  # Will be outlier
    ]
    
    thresholds = {
        'low': 40,
        'high': 50
    }
    
    final_score = process_metrics(data, thresholds)
    print(f"Result: {final_score}")