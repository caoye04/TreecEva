import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return [i ** 2 for i in x if i % 3 == 0]

# Decoy transformation with misleading intermediate results
def decoy_process(seq):
    temp = [math.sin(i) * 100 for i in seq]
    adjusted = [int(abs(t)) % 7 for t in temp]
    return sorted(adjusted, reverse=True)

# Actual data pipeline components
def filter_relevant(stream):
    return list(filter(lambda x: x > 0 and x % 2 == 1, stream))

def map_features(items):
    return [item * 3 + 2 for item in items]

def reduce_to_key(items):
    acc = 0
    for val in items:
        acc = (acc ^ val) * 2
        if acc > 1000:
            acc = acc // 3
    return acc % 97

# Complex transformation chain
def transform_signal(raw):
    step1 = [x + 5 for x in raw]
    step2 = [y for y in step1 if y % 4 != 0]
    step3 = [z * 2 for z in step2]
    return step3

# Red herring: bit manipulation that looks important but isn't used
def hidden_bit_analysis(data):
    result = 0
    for d in data:
        result ^= (d << 2) | (d >> 1)
        result = (result + 13) % 101
    return result

# Unused recursive distraction
def recursive_distractor(n):
    if n <= 1:
        return 1
    return n * recursive_distractor(n - 2) + 7

# Real processing functions
def finalize(data):
    base = sum(data) % 1000
    modifier = len([x for x in data if x % 3 == 0]) * 7
    return base - modifier + 13

def main():
    # Initial dataset
    sensor_readings = [12, 7, 3, 8, 15, 4, 9, 2, 6]
    
    # Irrelevant preprocessing (distractor)
    noise_profile = [r % 5 for r in sensor_readings]
    normalized = [math.log(r + 1) for r in sensor_readings]
    
    # Actual relevant data flow begins here
    filtered = filter_relevant(sensor_readings)
    enhanced = map_features(filtered)  # [7*3+2=23, 3*3+2=11, 15*3+2=47, 9*3+2=29]
    key_hash = reduce_to_key(enhanced)  # Used to seed something? Actually not.
    
    # Core transformation path
    processed_buffer = transform_signal(enhanced)  # Transform the enhanced values
    # enhanced = [23,11,47,29] → +5 → [28,16,52,34] → remove multiples of 4 → [11→16? no, wait: 28%4==0 → out, 16%4==0 → out, 52%4==0 → out, 34%4!=0 → keep? 34%4=2 → keep? Actually none from first pass...]
    # Correction: 23→28 (%4=0), 11→16 (%4=0), 47→52 (%4=0), 29→34 (%4=2 → keep)
    # So only 34 remains → then *2 → 68
    # processed_buffer = [68]
    
    # More distractions
    dummy_stats = {
        'peak': max(processed_buffer),
        'entropy': math.floor(sum(processed_buffer) / len(processed_buffer)),
        'flagged': any(x < 0 for x in processed_buffer)
    }
    
    # Another decoy usage
    _ = decoy_process(list(range(5)))
    
    # Finalization using the real logic
    core_output = finalize(processed_buffer)  # finalize([68])
    # sum = 68, len of multiples of 3: 68 % 3 != 0 → count = 0
    # → 68 % 1000 = 68, modifier = 0, +13 → 81
    
    # Print required output
    print(f"Result: {core_output}")

if __name__ == "__main__":
    main()