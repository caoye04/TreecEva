import math

def analyze_sensor(node_data, threshold=100):
    # Irrelevant data transformation (dead path)
    temp_log = [x * 1.8 + 32 for x in node_data if x > 0]
    processed = []
    for val in node_data:
        if val < 0:
            continue
        if val % 2 == 0:
            processed.append(int(math.sqrt(val)) if val > 10 else val)
        else:
            processed.append(val // 3)
    return processed

def filter_outliers(seq, limit=50):
    # Misleading function: looks important but used only once with non-impacting data
    return [x for x in seq if x <= limit]

def accumulate_energy(readings):
    total = 0
    factor = 1
    for r in readings:
        if r > 20:
            factor = 2
        total += r * factor
        # Decoy accumulation
        total -= max(0, r - 25) // 4
    return total

def compute_efficiency(raw, mode='balanced'):
    # Complex-looking efficiency with red herring bitwise ops
    base = sum(raw)
    shift = len(raw) & 3
    mask = (1 << shift) - 1
    masked = base & ~mask
    if mode == 'aggressive':
        return masked * 1.1
    elif mode == 'conservative':
        return masked * 0.9
    return masked  # 'balanced' mode

def transform_coordinates(x_list, y_list):
    # Distractor: unused later
    result = []
    for i, (x, y) in enumerate(zip(x_list, y_list)):
        result.append((x ^ i) | (y << 1))
    return result

def harvest_results(data_map):
    # Core logic hidden among distractions
    energy_pool = 0
    stats = {}
    for key, values in data_map.items():
        # Real processing begins
        filtered = [v for v in values if v % 2 == 1]  # Keep odd numbers
        if not filtered:
            stats[key] = 0
            continue
        # Sum odd values, apply decay based on count
        raw_sum = sum(filtered)
        decay_factor = 1 / (1 + math.log(len(filtered) + 1))
        adjusted = raw_sum * decay_factor
        energy_pool += adjusted
        stats[key] = len(filtered)
    
    # Critical distractors below
    decoy_sum = sum(stats.values()) * 0.5
    energy_pool -= decoy_sum  # Looks like correction, but small impact
    
    # Bitwise twist on final pool
    int_part = int(abs(energy_pool))
    fractional = energy_pool - int_part
    # XOR with length-derived pattern
    signature = int_part ^ (len(stats) << 4)
    final = signature + fractional
    
    # This line is critical
    final *= (1 + (len(data_map.get('sector_7', [])) > 0) * 0.25)  # Bonus if sector_7 has entries
    
    return round(final, 6)

# Main execution
if __name__ == '__main__':
    # Simulated sensor readings across zones (real input)
    zone_data = {
        'zone_a': [81, 16, 25, 36, 49],
        'zone_b': [10, 15, 20, 25, 30, 35],
        'zone_c': [7, 14, 21, 28],
        'sector_7': [11, 22, 33, 44, 55]  # Triggers bonus
    }

    # Dead preprocessing path
    coordinates_x = [1, 2, 3, 4]
    coordinates_y = [5, 6, 7, 8]
    _ = transform_coordinates(coordinates_x, coordinates_y)

    # Real pipeline starts here
    processed_data = {}
    for k, v in zone_data.items():
        analyzed = analyze_sensor(v)
        accumulated = accumulate_energy(analyzed)
        efficiency = compute_efficiency(analyzed)
        # Combine results meaningfully
        combined = [accumulated // 10, int(efficiency) % 50]
        processed_data[k] = analyzed + combined

    # Filtering that alters data slightly
    for k in processed_data:
        processed_data[k] = filter_outliers(processed_data[k], limit=40)

    # Final computation
    final_yield = harvest_results(processed_data)
    print(f"Result: {final_yield}")