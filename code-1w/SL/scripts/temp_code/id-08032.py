from collections import defaultdict

# Simulate sensor data processing with noise filtering and event detection
def main():
    raw_data = [14, 7, 22, 3, 9, 18, 5, 11, 6, 13, 8, 20]
    baseline = 10
    sensitivity = 2
    noise_floor = 4
    max_expected = 25

    # Irrelevant scaling factor (distractor)
    scaling_factor = 1.75
    scaled_values = [x * scaling_factor for x in raw_data]  # Not used later

    # Filter out low-amplitude noise
    filtered_data = [x for x in raw_data if x > noise_floor]

    # Detect events above dynamic threshold
    dynamic_offset = len(filtered_data) // 3
    detection_threshold = baseline + sensitivity + dynamic_offset

    # Count occurrences per magnitude band (semi-relevant)
    band_count = defaultdict(int)
    for val in filtered_data:
        band = (val // 5) * 5
        band_count[band] += 1

    # Extract significant events
    detected_events = [x for x in filtered_data if x >= detection_threshold]

    # Spurious statistical calculation (dead code path)
    avg_filtered = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    variance_proxy = sum((x - avg_filtered) ** 2 for x in filtered_data) / len(filtered_data) if filtered_data else 0
    stability_index = (avg_filtered / (variance_proxy + 1)) if variance_proxy > 0 else 0  # Unused

    # Threshold determined from band distribution
    dominant_band = max(band_count.keys(), key=lambda k: band_count[k]) if band_count else 0
    secondary_threshold = dominant_band + 5

    # Conditional expression to adjust threshold based on event density
    threshold = detection_threshold if len(detected_events) < 5 else min(detection_threshold, secondary_threshold)

    # Core processing function
    def process_signals(events, limit):
        if not events:
            return 0
        
        # Nested logic with accumulation
        adjusted = []
        for e in events:
            if e < baseline:
                adjusted.append(e * 2)
            elif e == baseline:
                adjusted.append(e + 1)
            else:
                # Complex conditional expression
                adj_val = e + 1 if (e % 2 == 0) else e - 1
                adjusted.append(adj_val)
        
        # Further filtering
        refined = [x for x in adjusted if x <= limit + 3]
        
        # Accumulate result with min constraint
        total = sum(refined)
        final = total if total <= max_expected else max_expected - 5
        
        # Dead computation branch (distractor)
        if total > 50:
            compensation_factor = 0.9
            rebalanced = [int(x * compensation_factor) for x in refined]
            final = sum(rebalanced)  # This block won't execute
            
        return final

    final_output = process_signals(detected_events, threshold)
    print(f"Result: {final_output}")

if __name__ == "__main__":
    main()