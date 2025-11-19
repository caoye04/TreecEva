import re
from collections import defaultdict

def defect_severity(hex_digit):
    if hex_digit.isdigit():
        return int(hex_digit) + 1
    else:
        return ord(hex_digit.upper()) - ord('A') + 11

def correction_factor(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    return dp[n]

def process_fabric_segments(segment_data):
    total_score = 0
    segment_count = 0
    
    for segment in segment_data:
        # Clean segment by removing non-hex characters
        clean_segment = re.sub(r'[^0-9A-Fa-f]', '', segment)
        if not clean_segment:
            continue
            
        # Count frequency of each hex digit
        freq_map = defaultdict(int)
        for char in clean_segment:
            freq_map[char.upper()] += 1
            
        # Calculate segment score
        segment_score = 0
        for digit, count in freq_map.items():
            severity = defect_severity(digit)
            segment_score += count * severity
            
        total_score += segment_score
        segment_count += 1
        
    # Apply correction factor
    if segment_count > 0:
        corr_factor = correction_factor(segment_count)
        final_metric = total_score * corr_factor
    else:
        final_metric = 0
        
    return final_metric

# Fabric segment data from quality control scans
fabric_segments = [
    "A1B2-C3D4",
    "EF56-7890",
    "aaBBccDD",
    "123!@#456",
    "FEDCBA98"
]

final_metric = process_fabric_segments(fabric_segments)
print(f"Result: {final_metric}")