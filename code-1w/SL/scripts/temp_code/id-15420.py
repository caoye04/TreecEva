import itertools

# Agricultural simulation: Crop yield optimization with noise and distractors

def simulate_growth(base, stress_factor):
    return (base * 1.2) - stress_factor

def calculate_resilience(index, diversity):
    return (index + diversity) // 1.5

def dummy_analysis(data):
    # Irrelevant function - dead code path
    return sum(x ** 0.5 for x in data if x > 5)

def decay_modifier(age):
    # Misleading computation - not actually used in final result
    if age < 3:
        return 0.95
    elif age < 7:
        return 0.88
    else:
        return 0.75

def evaluate_stability(readings):
    # Distractor: processes data but unused
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return variance < 2.0

def filter_active_blocks(zones):
    # Relevant: extracts zones with activity > threshold
    return [z for z in zones if z[1] > 12]

def transform_coordinates(coords):
    # Red herring: complex-looking math that isn't used
    transformed = []
    for x, y in coords:
        lat = (x * 0.87) + (y % 3)
        lon = (y * 1.03) - (x % 2)
        transformed.append((lat, lon))
    return transformed

def extract_signatures(sequence):
    # Unused feature engineering - distractor
    return [seq[-1] for seq in sequence if len(seq) >= 3]

def optimize_harvest(blocks):
    total = 0
    multiplier = 1.6
    for b in blocks:
        # Core logic: apply growth model and resilience adjustment
        raw_yield = simulate_growth(b[2], b[3])
        resilience = calculate_resilience(b[0], b[4])
        adjusted = raw_yield * (resilience / 100.0)
        total += adjusted
    return int(total * multiplier)

# Main execution
if __name__ == "__main__":
    # Simulated field block data: (id, activity, base_yield, stress, diversity)
    field_blocks = [
        (1, 15, 88, 7.2, 6),
        (2, 8, 76, 5.1, 4),  # Will be filtered out due to activity <= 12
        (3, 20, 94, 8.3, 7),
        (4, 10, 65, 4.0, 5),  # Filtered out
        (5, 18, 82, 6.7, 6)
    ]

    # Irrelevant coordinate grid
    gps_coords = [(100+i, 200+i*2) for i in range(5)]
    geo_references = transform_coordinates(gps_coords)

    # Distractor: sensor readings with stability check (unused)
    sensor_logs = [12.1, 13.5, 11.9, 14.2, 13.0]
    stable_system = evaluate_stability(sensor_logs)

    # Distractor: signature extraction from dummy sequences
    event_sequence = [[1,2], [3,4,5], [6,7], [8,9,10,11]]
    signatures = extract_signatures(event_sequence)

    # Real processing begins here
    active_blocks = filter_active_blocks(field_blocks)  # Filters to blocks 1,3,5

    # Additional irrelevant transformation
    indexed_data = list(enumerate(active_blocks))
    paired_streams = list(zip([x[1][0] for x in indexed_data], [x[1][2] for x in indexed_data]))

    # Critical slicing operation - uses only specific elements
    processed_blocks = [(b[0], b[2], b[3], b[4]) for idx, b in indexed_data[::2]]  # Take every other block

    # Dummy analysis on unrelated metric
    dummy_values = [9, 12, 15, 7, 18]
    dummy_result = dummy_analysis(dummy_values)

    # Core calculation - this is where the answer comes from
    final_yield = optimize_harvest(processed_blocks)

    print(f"Result: {final_yield}")