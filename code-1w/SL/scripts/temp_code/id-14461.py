from itertools import groupby

def calculate_final_score(raw_data):
    # Preprocess: split string data into tokens and convert to integers
    tokenized = [list(map(int, segment.split(','))) for segment in raw_data]
    
    # Compute sum of each segment
    segment_sums = [sum(segment) for segment in tokenized]
    
    # Group consecutive equal values (for anomaly detection)
    grouped = [list(group) for key, group in groupby(segment_sums)]
    group_counts = [len(group) for group in grouped]
    
    # Base score is the sum of all segment sums
    base_score = sum(segment_sums)
    
    # Apply bonus: for each group of repeated segment sums, add square of group length
    bonus = sum(count**2 for count in group_counts if count > 1)
    
    # Final score calculation
    final_score = base_score + bonus
    
    return final_score

# Simulated input data: comma-separated numbers in multiple segments
data_segments = [
    "10,15,20",
    "25,30",
    "55",  # This equals previous sum (55)
    "10,10,10,10,15",
    "5,5,45"
]

result = calculate_final_score(data_segments)
print(f"Result: {result}")