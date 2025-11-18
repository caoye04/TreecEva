import re
from dataclasses import dataclass
from contextlib import contextmanager

def transform_header(header_str):
    # Step 1: Extract numeric components using regex
    numbers = re.findall(r'\d+', header_str)
    nums = [int(n) for n in numbers]
    
    # Step 2: Apply bitwise operations
    if len(nums) >= 2:
        xor_result = nums[0] ^ nums[1]
        shifted = xor_result << 2
        masked = shifted & 0xFF
    else:
        masked = 0
    
    # Step 3: String transformation
    clean_header = re.sub(r'[^a-zA-Z0-9]', '', header_str)
    char_sum = sum(ord(c) for c in clean_header)
    
    # Step 4: Sorting and divide-and-conquer max finding
    all_values = nums + [masked, char_sum % 100]
    all_values.sort()
    
    def find_max(arr, low, high):
        if low == high:
            return arr[low]
        mid = (low + high) // 2
        left_max = find_max(arr, low, mid)
        right_max = find_max(arr, mid+1, high)
        return max(left_max, right_max)
    
    max_val = find_max(all_values, 0, len(all_values)-1)
    
    # Step 5: Context manager for score calculation
    @contextmanager
    def threat_context():
        score_components = []
        try:
            yield score_components
        finally:
            pass
    
    with threat_context() as components:
        components.append(masked)
        components.append(char_sum % 100)
        components.append(max_val)
        
        # Final calculation
        threat_score = 0
        for i, comp in enumerate(components):
            if i == 0:
                threat_score += comp * 3
            elif i == 1:
                threat_score -= comp * 2
            else:
                threat_score += comp // 4
    
    return threat_score

# Main execution
packet_header = "TCP[123]:SRC_PORT=456&DST_PORT=789"
threat_score = transform_header(packet_header)
print(f"Result: {threat_score}")