def main():
    # Simulate industrial batch processing with quality filtering
    raw_input_data = '87,93,78,96,88,74,91,85,89,95'
    threshold = 85
    min_quality_score = 75
    scaling_factor = 1.5
    adjustment_offset = -2

    # Parse and filter batch scores
    string_values = raw_input_data.split(',')
    numeric_scores = [int(x.strip()) for x in string_values]

    # Apply conditional scaling to high-performing batches
    adjusted_scores = []
    for score in numeric_scores:
        if score >= threshold:
            boosted = score * scaling_factor
            adjusted_scores.append(int(boosted))
        else:
            adjusted_scores.append(score + adjustment_offset)

    # Track statistics (partially irrelevant)
    avg_pre = sum(numeric_scores) / len(numeric_scores)
    max_pre = max(numeric_scores)
    total_batches = len(numeric_scores)

    # Filter out low-quality batches post-adjustment
    filtered_batches = [b for b in adjusted_scores if b >= min_quality_score]

    # Simulate parallel processing lanes
    lane_a = filtered_batches[::2]
    lane_b = filtered_batches[1::2]
    lane_efficiency = lambda l: sum(l) / len(l) if l else 0

    efficiency_a = lane_efficiency(lane_a)
    efficiency_b = lane_efficiency(lane_b)

    # Compute overall throughput
    total_output = sum(filtered_batches)
    overhead_penalty = len(filtered_batches) * 0.1
    normalized_output = total_output - overhead_penalty

    # Calculate yield per original batch
    processed_batches = len(filtered_batches)
    base_yield_per_batch = normalized_output / total_batches

    # Auxiliary distraction: analyze score patterns
    pattern_tracker = {}
    for i, val in enumerate(numeric_scores):
        category = 'high' if val >= threshold else 'standard'
        pattern_tracker[i] = category.upper()[::-1]  # Reversed for no reason

    extra_computation = sum([len(s) for s in pattern_tracker.values()])
    dummy_shift = extra_computation >> 2

    # Core calculation
    def calculate_production_efficiency(count):
        base = base_yield_per_batch
        if count > 7:
            return base * 1.25 + dummy_shift
        elif count > 5:
            return base * 1.15 + dummy_shift
        else:
            return base + dummy_shift

    final_yield = calculate_production_efficiency(processed_batches)
    final_yield = round(final_yield, 4)

    print(f"Result: {final_yield}")

if __name__ == "__main__":
    main()