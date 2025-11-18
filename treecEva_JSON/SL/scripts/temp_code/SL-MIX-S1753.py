from collections import defaultdict, deque

def decode_dna_sequence(encoded_str):
    mapping = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(mapping.get(char, char) for char in encoded_str)

def calculate_gc_content(sequence):
    gc_count = sum(1 for base in sequence if base in 'GC')
    return (gc_count / len(sequence)) * 100 if sequence else 0

def process_genomic_data():
    # Initial encoded sequences
    raw_sequences = ['ATCG', 'GGCC', 'TTAA']
    
    # Step 1: Decode all sequences
    decoded_pool = [decode_dna_sequence(seq) for seq in raw_sequences]
    
    # Step 2: Filter sequences with GC content > 50%
    high_gc_sequences = [seq for seq in decoded_pool if calculate_gc_content(seq) > 50]
    
    # Step 3: Build complement frequency map
    complement_freq = defaultdict(int)
    for seq in high_gc_sequences:
        for base in seq:
            complement_freq[base] += 1
    
    # Step 4: Process with queue-based sliding window
    window_queue = deque(maxlen=3)
    window_values = []
    
    # Flatten the high GC sequences
    flattened = ''.join(high_gc_sequences)
    
    for char in flattened:
        window_queue.append(ord(char))
        if len(window_queue) == 3:
            window_sum = sum(window_queue)
            window_values.append(window_sum)
            window_queue.popleft()
    
    # Step 5: Encode final result
    if not window_values:
        return 0
        
    max_window = max(window_values)
    min_window = min(window_values)
    
    # Final encoding step
    final_code = (max_window << 2) ^ min_window
    return final_code

final_code = process_genomic_data()
print(f"Result: {final_code}")