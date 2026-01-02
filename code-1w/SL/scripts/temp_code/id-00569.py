from itertools import compress, count

# Simulate sensor data filtering and efficiency calculation in an industrial monitoring system
def main():
    raw_readings = [104, 95, 110, 90, 120, 85, 130, 78, 135, 88]
    baseline = 100
    tolerance = 15
    threshold = 92

    # Identify stable readings within acceptable deviation from baseline
    is_stable = lambda x: abs(x - baseline) <= tolerance
    filtered_readings = list(filter(is_stable, raw_readings))

    # Generate sequence indices for tracking
    indices = count(1)
    indexed_data = {next(indices): val for val in raw_readings}

    # Misleading transformation: normalized values (not used in final calculation)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), 4) for x in raw_readings]

    # Simulate packet loss in transmission: every 3rd element dropped
    mask = [i % 3 != 0 for i in range(len(raw_readings))]
    transmitted_data = list(compress(raw_readings, mask))

    # Correct processing path: only filtered_readings are relevant
    valid_count = len(filtered_readings)
    total_fluctuation = sum(abs(filtered_readings[i] - filtered_readings[i-1]) 
                           for i in range(1, len(filtered_readings))) if valid_count > 1 else 0

    # Auxiliary diagnostic metric (distractor)
    avg_gap = total_fluctuation / (valid_count - 1) if valid_count > 1 else 0

    # Core logic for efficiency score
    def calculate_efficiency(data, min_threshold):
        above_min = [x for x in data if x >= min_threshold]
        if not above_min:
            return 0
        return int(sum(above_min) / len(above_min)) - baseline

    # Key execution point
    efficiency_score = calculate_efficiency(filtered_readings, threshold)

    # Red herring: unused correction factor
    correction_factor = round(avg_gap * 0.75, 3)

    # Print result for evaluation
    print(f"Result: {efficiency_score}")

if __name__ == "__main__":
    main()