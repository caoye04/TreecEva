import math

def collect_metrics(data_stream):
    # Irrelevant aggregation function (dead path)
    cumulative = 0
    for val in data_stream:
        cumulative += val ** 2
    return cumulative // len(data_stream) if data_stream else 0

def parse_timestamp(log_entry):
    # Distractor: timestamp logic not used in final computation
    hours = int(log_entry[0:2])
    minutes = int(log_entry[2:4])
    seconds = int(log_entry[4:6])
    return hours * 3600 + minutes * 60 + seconds

def filter_anomalies(readings):
    # Extract only readings with prime index positions (real logic)
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    filtered = []
    for idx, val in enumerate(readings):
        if is_prime(idx):  # Only include values at prime indices
            filtered.append(val)
    
    # Decoy operation: unused transformation
    inverted = [1.0 / x for x in readings if x != 0]
    normalizations = sum([x*x for x in filtered])
    
    return set(filtered)  # Return as set for later intersection logic

def generate_baseline(count):
    # Irrelevant baseline generation (misleading)
    base = 1
    sequence = []
    for i in range(count):
        base = (base * 7) % 101
        sequence.append(base)
    return sequence

def analyze_readings(valid_set):
    # Core logic: compute product of digits across all numbers, then mod 1e6
    digit_product = 1
    total_digits = 0
    
    for num in valid_set:
        # Decompose each number into digits
        temp = abs(int(num))
        if temp == 0:
            digit_product *= 1
            total_digits += 1
            continue
        while temp > 0:
            digit = temp % 10
            if digit != 0:  # Ignore zero digits
                digit_product = (digit_product * digit) % 1000000
            temp //= 10
            total_digits += 1
    
    # Secondary metric: average magnitude (distractor)
    avg_mag = sum(abs(x) for x in valid_set) / len(valid_set) if valid_set else 0
    
    # Real answer derived from digit product
    result = digit_product % 1000000
    
    # Dead branch: never executed due to constant guard
    if False and len(valid_set) > 100:
        fallback = 0
        for x in valid_set:
            fallback += hash(str(x))
        result = fallback % 1000000
    
    return result

def main():
    # Simulated sensor cluster output
    sensor_cluster = [
        23, 45, 17, 88, 91, 103, 44, 107, 113, 120, 127, 131, 137, 139, 149
    ]
    
    # Unused transformations (red herrings)
    timestamps = ['081523', '081601', '081645', '081729']
    parsed_times = [parse_timestamp(ts) for ts in timestamps]
    baseline_ref = generate_baseline(20)
    metrics = collect_metrics(sensor_cluster)
    
    # Core processing chain
    anomalies_filtered = filter_anomalies(sensor_cluster)
    final_diagnostic = analyze_readings(anomalies_filtered)
    
    # Additional distraction: tuple unpacking and unused combinatorics
    stats_summary = (len(anomalies_filtered), min(anomalies_filtered), max(anomalies_filtered))
    count, low, high = stats_summary
    mid_range = (low + high) / 2
    
    # Character counting decoy
    label = "sensor_diagnostic_v1"
    char_freq = {}
    for c in label:
        char_freq[c] = char_freq.get(c, 0) + 1
    vowel_count = sum(char_freq.get(v, 0) for v in 'aeiou')
    
    # Final output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()