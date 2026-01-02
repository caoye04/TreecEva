import math

def analyze_frequency(signal):
    magnitude = sum([x ** 2 for x in signal])
    avg = sum(signal) / len(signal)
    variance = sum((x - avg) ** 2 for x in signal) / len(signal)
    normalized = [x / (magnitude ** 0.5) for x in signal]
    return normalized, magnitude

def generate_pattern(base_seq, shift):
    shifted = [(x + shift) % 8 for x in base_seq]
    doubled = [x * 2 for x in shifted]  # distractor: not used later
    modded = [x % 7 for x in doubled]
    return modded

def calculate_interference(a, b):
    total = 0
    phase_weights = []
    for i, (x, y) in enumerate(zip(a, b)):
        diff = abs(x - y)
        weight = math.cos(diff)
        phase_weights.append(weight)
        if diff > 3:
            total += int(weight * 2)
        else:
            total -= int(weight)
    
    # Distractor: extra tracking variables
    stats = {}
    for idx, val in enumerate(phase_weights):
        stats[f'entry_{idx}'] = round(val, 3)
    
    # Real computation path
    adjustment = 0
    for i in range(len(a)):
        if a[i] % 2 == 0 and b[i] % 2 == 1:
            adjustment += 1
    total += adjustment * 2

    # Dead code branch (never executed due to data)
    if max(a) > 20:
        fallback = sum(a) // len(a)
        total = fallback

    return total

def main():
    raw_data = [1, 3, 2, 6, 4, 5]
    processed, energy = analyze_frequency(raw_data)
    
    # Generate two interference patterns
    pattern_a = generate_pattern(raw_data, shift=2)
    pattern_b = generate_pattern(raw_data, shift=5)
    
    # Tracking variables with limited relevance
    entropy_estimate = 0.0
    for p in processed:
        if p > 0.1:
            entropy_estimate -= p * math.log(p)
    
    # Key computation
    net_phase_shift = calculate_interference(pattern_a, pattern_b)
    
    # Additional irrelevant transformations
    squared_chain = [x**2 for x in pattern_a if x % 2 == 0]
    filtered_sum = sum(squared_chain)
    
    print(f"Result: {net_phase_shift}")

if __name__ == "__main__":
    main()