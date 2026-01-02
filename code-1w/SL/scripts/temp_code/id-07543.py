def analyze_sequence(data):
    count = 0
    total = 0
    temp_result = []
    
    # Irrelevant tracking variables (distractors)
    max_val = float('-inf')
    min_val = float('inf')
    outlier_detected = False
    normalization_factor = 1.0
    
    for i, x in enumerate(data):
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x

        # Real logic: accumulate every even index value
        if i % 2 == 0:
            total += x * (i + 1)

        # Dead code path - never executed due to logic
        if len(temp_result) > 100:
            normalization_factor = sum(temp_result) / len(temp_result)

    # Another decoy function embedded as lambda (not used)
    validate = lambda x: (x % 7 == 0) and (x > 50)
    candidates = [x for x in data if validate(x)]  # Unused list

    # Secondary distraction: character counting in string representation
    digit_count = {str(i): 0 for i in range(10)}
    for d in data:
        for c in str(d):
            if c.isdigit():
                digit_count[c] += 1
    
    # Unused transformation map
    transform_map = dict(zip(data, [d ** 0.5 for d in data]))

    return total


def process_segments(segments):
    results = []
    for seg in segments:
        # Misleading intermediate summation
        segment_sum = sum(seg)
        adjusted_sum = segment_sum // 2 if len(seg) > 3 else segment_sum
        results.append(adjusted_sum)
    return results

# Decoy recursive function (never called)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Real but obscured core logic
def finalize(value, key):
    # Bit manipulation red herring
    masked = value ^ (key << 2)
    shifted = masked >> 1
    
    # Actual answer computation hidden among noise
    result = (shifted + key) % 97
    return result

# Unused data structure with cross-reference
class DataNode:
    def __init__(self, val):
        self.val = val
        self.ref = None

nodes = [DataNode(x) for x in [10, 20, 30]]
nodes[0].ref = nodes[1]

# Main execution flow
if __name__ == "__main__":
    raw_data = [4, 8, 5, 12, 6, 18, 7, 9]
    segments = [[4, 8], [5, 12, 6], [18, 7, 9]]
    
    # Distractor: unused processed segments
    processed = process_segments(segments)
    
    # Core relevant computation
    summation = analyze_sequence(raw_data)
    
    # Pivot derived from conditional expression (real use)
    pivot = 42 if any(x > 15 for x in raw_data) else 24
    
    # Critical statement
    checksum = finalize(summation, pivot)
    
    # Output required format
    print(f"Result: {checksum}")