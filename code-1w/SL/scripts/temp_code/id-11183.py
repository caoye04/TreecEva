import itertools

def analyze_sequence(data):
    # Irrelevant analysis function (dead code path)
    return sum(x ** 2 for x in data if x % 3 == 0)

def preprocess_signal(signal):
    # Distractor: signal processing that isn't used in final result
    filtered = [x for x in signal if x > 0]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return [int(n * 100) for n in normalized]

def transform_keypoints(points):
    # Bit manipulation red herring
    shifted = [(p << 1) ^ 255 for p in points]
    return [s & 127 for s in shifted]

def compute_entropy(sequence):
    # Complex-looking but unused entropy calculation
    freq = {x: sequence.count(x) for x in set(sequence)}
    total = len(sequence)
    from math import log2
    return round(-sum((count/total) * log2(count/total) for count in freq.values()), 4)

def evaluate_baseline(baseline):
    # Partially relevant but ultimately misleading
    temp = 0
    for i in range(len(baseline)):
        if i % 2 == 0:
            temp += baseline[i] * 2
        else:
            temp -= baseline[i] // 3
    return temp // 5  # Dead-end computation

def evaluate_performance(metrics, reference):
    # Core logic hidden among distractions
    pivot = sum(reference) // len(reference)
    
    # Real computation begins here
    adjusted = [m + (i % 4) for i, m in enumerate(metrics)]
    
    # Key transformation with list comprehension and itertools
    paired = list(itertools.zip_longest(adjusted, reference, fillvalue=0))
    scores = []
    
    for a, b in paired:
        diff = abs(a - b)
        if diff == 0:
            score = 10
        elif diff < 5:
            score = 5
        elif diff < 10:
            score = 2
        else:
            score = -1
        scores.append(score)
    
    # Actual answer derived here through conditional weighting
    weighted = [s * (1 + (idx % 3)) for idx, s in enumerate(scores)]
    aggregate = sum(weighted)
    
    # Misleading normalization path
    peak = max(weighted)
    normalized_result = aggregate / (peak if peak != 0 else 1)
    
    # Final score uses raw aggregate, not normalized
    final_score = aggregate + 17  # Critical offset
    
    # Decoy operations below
    checksum = sum(final_score.to_bytes(4, 'big'))
    verification = (checksum ^ 0xFF) & 0x7F
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Irrelevant data structures
    sensor_log = [23, 15, 88, 41, 26, 77, 33]
    timing_frames = [95, 12, 64, 29, 55]
    key_points = [100, 200, 300, 400]

    # Distractor preprocessing
    processed_signal = preprocess_signal(timing_frames)
    transformed = transform_keypoints(key_points)
    dummy_entropy = compute_entropy(sensor_log)

    # Relevant inputs hidden among noise
    metrics = [8, 12, 5, 18, 3, 9]
    baseline = [6, 10, 7, 15, 4, 8]

    # Unused recursive red herring
    def recursive_waste(n):
        if n <= 1:
            return 1
        return recursive_waste(n-1) + recursive_waste(n-2)
    
    waste_result = recursive_waste(6)  # Computationally expensive but unused

    # Key execution point
    final_score = evaluate_performance(metrics, baseline)
    
    # Output required format
    print(f"Result: {final_score}")