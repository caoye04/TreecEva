import itertools
import statistics

def process_waveform_segment(segment_data, mask_pattern):
    transformed_values = []
    for segment in segment_data:
        # Apply XOR mask and shift operations
        masked = segment ^ mask_pattern
        shifted = (masked << 1) & 0xF  # Keep within 4-bit range
        transformed_values.append(shifted)
    return transformed_values

def main():
    # Signal segments represented as 4-bit integers
    signal_segments = [
        [3, 7, 11, 15],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [0, 4, 8, 12]
    ]
    
    mask_sequence = [3, 5, 9, 6]
    accumulator = []
    
    # Nested loop processing
    for i, segment_group in enumerate(signal_segments):
        current_mask = mask_sequence[i]
        group_results = process_waveform_segment(segment_group, current_mask)
        accumulator.extend(group_results)
    
    # Compute statistical measure
    processed_mean = statistics.mean(accumulator)
    print(f"Result: {processed_mean}")
    return processed_mean

if __name__ == "__main__":
    main()