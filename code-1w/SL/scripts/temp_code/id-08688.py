from collections import defaultdict, Counter

# Simulate sensor data with noise and redundancy
def preprocess_sensor_readings(raw_readings):
    filtered = []
    outlier_count = 0
    temp_sum = 0

    for val in raw_readings:
        if val < 0 or val > 1000:  # Invalid range
            outlier_count += 1
            continue
        if val % 7 == 0:  # Red herring: irrelevant filtering
            temp_sum += val * 0.1
        else:
            filtered.append(val)

    # Misleading computation (not used later)
    average_outlier_proximity = temp_sum / (outlier_count + 1)

    return filtered

def aggregate_by_category(data):
    category_map = defaultdict(list)
    for item in data:
        key = 'even' if item % 2 == 0 else 'odd'
        category_map[key].append(item)
    
    # Extra processing with side results
    stats = {}
    for k, v in category_map.items():
        stats[k] = {
            'count': len(v),
            'sum': sum(v),
            'mode_freq': max(Counter(v).values()) if v else 0
        }
    
    # Distractor: unused transformation
    normalized = [x / (sum(data) * 0.01 + 1) for x in data]

    return category_map, stats

def calculate_final_score(data_dict):
    score = 0
    penalty = 0

    for key, values in data_dict.items():
        base = sum(values)
        if key == 'even':
            score += base // 10
        elif key == 'odd':
            score += len(values) * 5
            # Artificial complexity
            for v in values:
                if v % 3 == 0:
                    penalty += 1

    # Final adjustment with distractor variables
    debug_factor = len(data_dict.get('even', [])) + len(data_dict.get('odd', []))
    adjustment = 1 if debug_factor > 5 else 0  # Unused logic branch

    return score - penalty

# Main execution flow
if __name__ == '__main__':
    raw_data = [15, 22, 34, 45, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]
    
    # Step 1: Preprocess
    cleaned = preprocess_sensor_readings(raw_data)
    
    # Step 2: Aggregate
    grouped_data, summary_stats = aggregate_by_category(cleaned)
    
    # Step 3: Calculate final score
    final_score = calculate_final_score(grouped_data)
    
    # Print result as required
    print(f"Result: {final_score}")