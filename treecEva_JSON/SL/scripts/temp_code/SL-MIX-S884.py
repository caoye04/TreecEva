import re
from itertools import compress

def calculate_packet_score(header):
    # Extract numeric values from header using regex
    numbers = [int(x) for x in re.findall(r'\d+', header)]
    if not numbers:
        return 0
    
    # Apply bitwise operations on first two numbers
    xor_result = numbers[0] ^ numbers[1] if len(numbers) > 1 else numbers[0]
    
    # Check if any number is divisible by 7 (potential threat signature)
    has_seven_multiple = any(n % 7 == 0 for n in numbers)
    
    # Calculate base score using list comprehension
    base_scores = [n * 2 if n % 2 == 0 else n * 3 for n in numbers]
    total_base = sum(base_scores)
    
    # Adjust score based on threat signature
    adjusted_score = total_base + (xor_result if has_seven_multiple else 0)
    return adjusted_score

# Process packet headers
packet_headers = [
    "SRC:192.168.1.10 DST:10.0.0.5 PRT:8080 TTL:64",
    "SRC:172.16.0.25 DST:192.168.0.1 PRT:22 TTL:128 SEQ:1001",
    "SRC:10.0.0.15 DST:8.8.8.8 PRT:53 TTL:255 SEQ:2048 CHK:77"
]

# Use lambda to filter headers containing 'SEQ' field
seq_filter = lambda header: 'SEQ:' in header
filtered_headers = list(filter(seq_filter, packet_headers))

# Calculate scores for filtered headers
packet_scores = [calculate_packet_score(header) for header in filtered_headers]

# Binary search helper for finding score thresholds
def binary_search(scores, target):
    left, right = 0, len(scores) - 1
    while left <= right:
        mid = (left + right) // 2
        if scores[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

# Find index where scores exceed threshold of 1000
threshold_index = binary_search(sorted(packet_scores), 1000)

# Use itertools.compress to select scores above median
sorted_scores = sorted(packet_scores)
median = sorted_scores[len(sorted_scores)//2]
selector = [score > median for score in packet_scores]
selected_scores = list(compress(packet_scores, selector))

# Final threat score calculation
final_threat_score = sum(selected_scores) + threshold_index
print(f"Result: {final_threat_score}")