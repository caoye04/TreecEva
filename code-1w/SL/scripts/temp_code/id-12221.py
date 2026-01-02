def main():
    # Simulating a data processing pipeline with intermediate stages
    raw_data = [3, 5, 8, 13, 21]
    
    # Irrelevant transformation: reverse and square (not used in final path)
    reversed_squares = [x**2 for x in reversed(raw_data)]
    temp_offset = sum(reversed_squares) // len(reversed_squares)

    # Relevant transformations
    filtered = [x for x in raw_data if x % 2 == 1]  # Keep odd numbers
    mapped = list(map(lambda x: x * 2 + 1, filtered))  # Transform each

    # Intermediate aggregation
    running_total = 0
    history = []
    for val in mapped:
        running_total += val
        history.append(running_total)
    
    # Dummy conditional that doesn't affect outcome
    threshold = 10
    if len(history) > threshold:
        adjustment = -999  # Dead code path
    else:
        adjustment = 0  # Actually taken, but adds no effect

    # Additional distraction: set operations with unused result
    unique_values = set(mapped)
    duplicates_check = len(mapped) - len(unique_values)
    shadow_sum = sum([x for x in unique_values if x > 10])  # Computed but unused

    # Key accumulation using dictionary-based frequency tracking (semi-relevant)
    freq_map = {x: mapped.count(x) for x in mapped}
    weighted_sum = sum(k * v for k, v in freq_map.items())

    # Secondary processing chain
    squared_evens = [x**2 for x in raw_data if x % 2 == 0]
    offset_correction = len(squared_evens) * 2

    # Nested helper logic
    def calculate_base(sequence):
        return sum(sequence) // len(sequence)

    def calculate_final(results):
        base = calculate_base(results)
        bonus = len(results) * 3
        penalty = 0
        for r in results:
            if r > 20:
                penalty += 1
        return base + bonus - penalty

    pipeline_results = [weighted_sum, running_total, shadow_sum, temp_offset]
    
    # Unused debugging print
    # print(f'Debug: {pipeline_results}')

    final_score = calculate_final(pipeline_results)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()