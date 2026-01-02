from itertools import combinations

def classify_segment(a, b):
    if a + b > 10:
        return 'long'
    return 'short'

def process_segments(segments):
    classifications = [classify_segment(a, b) for a, b in segments]
    unique_classes = set(classifications)
    count_long = classifications.count('long')
    
    # Generate all pairs of segments that form closed loops (a+b == c+d)
    loop_count = 0
    for (a1, b1), (a2, b2) in combinations(segments, 2):
        if a1 + b1 == a2 + b2:
            loop_count += 1
            
    intermediate = len(unique_classes) * count_long
    result = intermediate + loop_count
    return result

# Irrelevant distraction: unused variable
baseline_offset = 7

segments = [(2, 9), (3, 4), (6, 5), (1, 2)]
result = process_segments(segments)
print(f"Target result: {result}")