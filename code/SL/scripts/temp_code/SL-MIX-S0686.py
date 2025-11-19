from functools import reduce
import itertools

def decode_hex_pattern(hex_string):
    # Convert hex string to list of integers
    return [int(char, 16) for char in hex_string]

def calculate_cluster_weights(defect_list):
    # Apply weighted scoring: first defect counts double, last defect counts half (rounded down)
    if len(defect_list) <= 1:
        return defect_list
    weighted = defect_list.copy()
    weighted[0] *= 2
    weighted[-1] //= 2
    return weighted

def apply_adaptive_filter(weighted_defects):
    # Recursively smooth the values using adjacent averaging
    def smooth(values, index=1):
        if index >= len(values) - 1:
            return values
        avg = (values[index-1] + values[index] + values[index+1]) // 3
        values[index] = avg
        return smooth(values, index + 1)
    
    if len(weighted_defects) < 3:
        return weighted_defects
    return smooth(weighted_defects.copy())

def compute_quality_score(processed_values):
    # State machine for quality assessment
    state = 'NORMAL'
    score = 0
    
    for val in processed_values:
        if state == 'NORMAL':
            if val > 10:
                state = 'ALERT'
                score += val * 2
            else:
                score += val
        elif state == 'ALERT':
            if val < 5:
                state = 'RECOVERY'
                score -= val
            else:
                score += val * 3
        elif state == 'RECOVERY':
            if val > 8:
                state = 'ALERT'
                score += val * 2
            else:
                score += val
    
    return score

def main():
    # Initial encoded defect pattern
    encoded_pattern = "B3F7A2"
    
    # Step 1: Decode hex pattern
    defect_clusters = decode_hex_pattern(encoded_pattern)
    
    # Step 2: Calculate weights
    weighted_defects = calculate_cluster_weights(defect_clusters)
    
    # Step 3: Apply adaptive filter
    smoothed_defects = apply_adaptive_filter(weighted_defects)
    
    # Step 4: Compute final quality score
    final_score = compute_quality_score(smoothed_defects)
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()