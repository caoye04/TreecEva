from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def validate_input(data):
    return isinstance(data, list) and all(isinstance(x, int) for x in data)

# Misleading transformation chain
def dummy_transform(seq):
    shifted = [x << 1 for x in seq]  # Bit shift - looks important
    normalized = [x % 100 for x in shifted]
    return [math.sin(x) for x in normalized]  # Unused result

def preprocess_items(raw):
    # Real preprocessing starts here
    temp = [x for x in raw if x > 0]
    counted = Counter(temp)
    frequency_map = defaultdict(int)
    for k, v in counted.items():
        frequency_map[k] = v * (k % 7)
    
    # Dead code path (early exit never taken due to data)
    if sum(temp) < 0:
        return [-1] * len(temp)
    
    # Actual relevant transformation
    transformed = []
    for item in temp:
        if item % 3 == 0:
            transformed.append(item ** 2)
        elif item % 5 == 0:
            transformed.append(item * 2)
        else:
            transformed.append(item + 1)
    return transformed

# Complex conditional analysis with red herring parameters
def analyze_pattern(data, reference):
    total = 0
    penalty = 0
    bonus = 0
    
    # Irrelevant tracking variables
    history = []
    debug_log = defaultdict(list)
    
    for i, val in enumerate(data):
        # Real logic embedded in noise
        if i >= len(reference):
            break
        
        # Key logic: XOR-based validation
        expected = reference[i]
        observed = val % 1000
        
        # Core comparison
        if (expected ^ observed) % 4 == 0:  # Critical condition
            total += observed // 4
        else:
            penalty += 1
        
        # Distracting logging
        debug_log['checks'].append({
            'index': i,
            'diff': abs(expected - observed),
            'status': 'passed' if (expected ^ observed) % 4 == 0 else 'failed'
        })
        
        # Unused bonus rule (never triggered due to design)
        if val > 100 and expected > 100 and i % 7 == 0:
            bonus += 5
    
    # Final score depends only on total - penalty irrelevant
    final = total - penalty  # But penalty never affects outcome
    return final

# Obfuscating setup block
def main():
    # Input data with mixed relevance
    raw_input = [3, -2, 6, 15, 7, 9, 25, -1, 12]
    key_reference = [9, 15, 36, 30, 8]  # Must align with transformed positions
    
    # Irrelevant secondary sequence
    auxiliary_seq = [x * 3 + 1 for x in range(8) if x % 2 == 0]
    shadow_copy = auxiliary_seq.copy()
    
    # Apply real preprocessing
    processed = preprocess_items(raw_input)
    
    # Transform again through decoy (unused)
    dummy_result = dummy_transform(processed)
    
    # Critical assignment point
    transformed_data = processed[:5]  # Truncate to match reference length
    
    # Key statement containing target variable
    final_score = analyze_pattern(transformed_data, key_reference)
    
    # Print required output
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()