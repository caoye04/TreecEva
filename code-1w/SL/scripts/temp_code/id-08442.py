import itertools

def main():
    # Simulated sensor data acquisition (irrelevant preprocessing)
    raw_samples = [i * 0.01 for i in range(1000)]
    scaled_data = [x * 1.03 for x in raw_samples if x > 0.5]  # Distraction: unused later

    # Core signal processing chain
    timestamps = list(range(500))
    base_wave = [abs((t % 25) - 12) / 12.0 for t in timestamps]
    noise_floor = sum([0.02 * ((t % 7) == 0) for t in timestamps])  # Red herring statistic

    # Frame segmentation with conditional logic
    frames = []
    for i in range(0, len(base_wave), 10):
        frame = base_wave[i:i+10]
        if len(frame) == 10 and sum(frame) > 5.0:
            frames.append([round(x + 0.01, 4) for x in frame])

    # Decoy transformation (never used)
    inverted_frames = [[1.0 - val for val in f] for f in frames if sum(f) < 1.0]  

    # Real processing path begins
    processed_frames = []
    buffer = []
    for idx, f in enumerate(frames):
        shifted = [v * (idx % 3 + 1) for v in f]  # Amplify by frame index pattern
        filtered = [v for v in shifted if v > 0.5]
        if len(filtered) >= 3:
            average_val = sum(filtered) / len(filtered)
            buffer.append(round(average_val, 4))
            if len(buffer) == 3:
                break  # Early exit condition (critical control flow)

    # Diagnostic computation using itertools
    expanded_buffer = list(itertools.chain.from_iterable([buffer] * 2))  # Double the sequence
    differences = [abs(expanded_buffer[i] - expanded_buffer[i-1]) for i in range(1, len(expanded_buffer))]
    mean_diff = sum(differences) / len(differences)

    # Auxiliary statistics (mostly irrelevant)
    spike_count = len([d for d in differences if d > 0.1])
    coherence_score = (len(buffer) / 3.0) if spike_count < 10 else 0.0  # Unused metric

    # Key function with nested logic and conditional expression
    def analyze_signal(data):
        if not data:
            return -1
        total = sum(data)
        size_factor = len(data) if len(data) < 10 else 10
        adjustment = 0.95 if any(x > 0.8 for x in data) else 1.05
        # Complex derived value using multiple concepts
        temp_result = (total * size_factor) * adjustment
        
        # Final branching logic with distractor variables
        threshold_met = temp_result > 10.0
        debug_flag = False  # Dead variable
        override_mode = False  # Never activated flag
        
        # Critical decision point
        final_value = temp_result * 1.1 if threshold_met else temp_result * 0.9
        return round(final_value, 4)

    # Execution point of interest
    final_diagnostic = analyze_signal(processed_frames)
    
    # Print required result
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()