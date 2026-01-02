def analyze_system_health(reading_stream, base_threshold):
    # Irrelevant pre-processing (distractor)
    normalized = [x * 0.98 + 2 for x in reading_stream if x > 50]
    outliers = [i for i, x in enumerate(reading_stream) if x > 100]
    adjusted = [x // 3 for x in normalized if x % 2 == 0]

    # Core logic disguised among distractions
    cumulative_score = 0
    temp_registry = []
    for idx, val in enumerate(reading_stream):
        if idx % 4 == 0:
            cumulative_score += val % 17
        elif val < base_threshold:
            cumulative_score -= (base_threshold - val) // 5

    # Dead code path (never reached due to logic above)
    redundant_calc = None
    if len(outliers) > 100:
        redundant_calc = sum([x ** 0.5 for x in adjusted])

    # Another distraction: string-based encoding of status (not used)
    status_flag = ''.join([chr(97 + (val % 26)) for val in reading_stream[:5]])

    # Actual relevant transformation (hidden in noise)
    def extract_signatures(data, factor):
        signatures = []
        for i, v in enumerate(data):
            if i % 3 == 2:
                signatures.append((v * factor) % 89)
        return signatures

    # Misleading secondary function definition (not used in final path)
    def deprecated_aggregator(seq):
        return sum(x & 15 for x in seq) * 2

    # Key data used later
    critical_readings = [x for x in reading_stream if 60 <= x <= 85]
    
    # Real processing begins here (buried)
    def process_metrics(logs, limits):
        total = 0
        phase_shift = limits['high'] // 11
        readings = [x for x in logs if isinstance(x, int) and x > 0]

        # Use of zip and enumerate together (required feature)
        for i, (a, b) in enumerate(zip(readings, readings[1:])):
            if i % 2 == 1:
                total += (a ^ b) % 13
            else:
                total -= (a + b) % 7

        # Slicing operation (required feature)
        subset = readings[-len(readings)//2:]
        
        # List comprehension with filtering (required feature)
        transformed = [((x >> 2) + phase_shift) * 3 for x in subset if x % 4 != 0]

        # Final computation chain
        intermediate = sum(transformed[:10]) // len(transformed) if transformed else 0
        checksum = sum(transformed) % 101
        return (intermediate * 17) - checksum + (phase_shift * 3)

    # Unused decoy call
    _ = extract_signatures(reading_stream, 5)

    # Define inputs for actual execution
    thresholds = {'low': 55, 'high': 97}
    log_data = [73, 68, 82, 59, 77, 88, 64, 71, 79, 66, 85, 74, 90, 81, 69]
    
    # Critical assignment
    final_diagnostic = process_metrics(log_data, thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")

# Simulate input data and execute
analyze_system_health([75, 80, 85, 90, 95, 100, 70, 65, 60, 55, 50, 45, 40, 35, 30], 60)