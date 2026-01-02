def analyze_pattern(sequence):
    count_a = sequence.count('A')
    count_t = sequence.count('T')
    count_g = sequence.count('G')
    count_c = sequence.count('C')
    total = len(sequence)
    
    # Distractor: GC content calculation (not used in final result)
    gc_content = (count_g + count_c) / total if total > 0 else 0
    
    # Distractor: Reverse complement logic (computed but not used)
    complement = str.maketrans('ATGC', 'TACG')
    reverse_complement = sequence.translate(complement)[::-1]
    
    # Relevant: Analyze periodicity of 'AT' motifs
    at_positions = []
    for i in range(len(sequence) - 1):
        if sequence[i:i+2] == 'AT':
            at_positions.append(i)
    
    # Compute average spacing between AT motifs
    if len(at_positions) > 1:
        spacings = [at_positions[i+1] - at_positions[i] for i in range(len(at_positions)-1)]
        avg_spacing = sum(spacings) / len(spacings)
    else:
        avg_spacing = 0
    
    # Return only the spacing (key signal)
    return avg_spacing


def extract_metadata(header):
    # Simulate parsing header with version, timestamp, checksum
    parts = header.split('|')
    version = parts[0].split('_')[1]
    timestamp = int(parts[1])
    checksum = int(parts[2])
    
    # Distractor: Validate checksum (executed but irrelevant)
    computed_checksum = sum(ord(c) for c in parts[0] + parts[1]) % 1000
    is_valid = computed_checksum == checksum
    
    # Return timestamp as base for later use
    return timestamp

def process_reads(reads):
    processed = []
    for read in reads:
        clean_read = read.strip().upper()
        # Filter only valid nucleotide sequences
        if all(c in 'ATGC' for c in clean_read) and len(clean_read) >= 5:
            processed.append(clean_read)
    return processed


def calculate_final_score(data):
    header = data['header']
    raw_reads = data['reads']
    
    # Step 1: Extract metadata (use timestamp)
    base_time = extract_metadata(header)
    
    # Step 2: Process and filter reads
    filtered_reads = process_reads(raw_reads)
    
    # Step 3: Analyze first valid read for AT pattern
    if not filtered_reads:
        pattern_metric = 0
    else:
        pattern_metric = analyze_pattern(filtered_reads[0])
    
    # Step 4: Compute auxiliary statistic - longest run of same base
    longest_run = 0
    if filtered_reads:
        for read in filtered_reads:
            current_run = 1
            max_in_read = 1
            for i in range(1, len(read)):
                if read[i] == read[i-1]:
                    current_run += 1
                else:
                    max_in_read = max(max_in_read, current_run)
                    current_run = 1
            max_in_read = max(max_in_read, current_run)
            longest_run = max(longest_run, max_in_read)
    
    # Distractor: Bitwise manipulation on timestamp (looks important)
    masked_time = base_time ^ 0xABCD
    time_flag = (masked_time >> 16) & 1
    
    # Step 5: Combine relevant metrics into score
    # Only pattern_metric and longest_run contribute
    intermediate = int(pattern_metric) * 3
    bonus = longest_run * 2
    final_score = intermediate + bonus + 5  # Final deterministic answer
    
    # Irrelevant print for distraction
    debug_value = (intermediate ^ bonus) & 0xFFFF
    
    return final_score

# Input data
data = {
    'header': 'v2|1984|723',
    'reads': [
        'atgcnnnn',
        'GGGTTATTAA',
        'NNNNN',
        'CCCGGGTTT'
    ]
}

# Execute
final_score = calculate_final_score(data)
print(f"Target result: {final_score}")