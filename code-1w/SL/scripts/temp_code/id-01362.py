import itertools

def main():
    # Sensor data simulation (real values)
    timestamps = list(range(100, 200, 5))
    base_readings = [t % 17 for t in timestamps]
    filtered_readings = [r for r in base_readings if r % 3 != 0]

    # Irrelevant auxiliary data (distractor)
    legacy_codes = ['A7', 'B9', 'C3', 'D1', 'E8']
    code_mapping = {code: idx * 100 for idx, code in enumerate(legacy_codes)}
    calibration_lookup = {i: i * 0.97 + 3 for i in range(50)}  # Unused

    # Core processing chain setup
    processing_chain = []
    for i, val in enumerate(filtered_readings):
        entry = {
            'id': i,
            'raw': val,
            'processed': (val ** 2) % 47,
            'flagged': val > 10,
            'aux': (i * val) % 19
        }
        processing_chain.append(entry)

    # Decoy transformation (never used)
    def transform_legacy(data_list):
        return [pow(d['raw'], 3, 59) for d in data_list if d['id'] % 4 == 0]

    decoy_output = transform_legacy(processing_chain)  # Dead assignment

    # Diagnostic engine with red herring logic
    diagnostics = []
    temp_accumulator = 0
    for idx, record in enumerate(processing_chain):
        if idx % 4 == 0:
            temp_accumulator += record['processed']
        elif idx % 4 == 2 and record['flagged']:
            temp_accumulator -= record['raw']

        # Real diagnostic signal buried in noise
        score = record['processed'] - record['raw']
        if record['aux'] % 5 == 0:
            score *= 2
        diagnostics.append(score)

    # Fake scoring model (distractor)
    def compute_legacy_score(seq):
        total = 0
        for s in seq:
            total += pow(s, 3) % 101
        return total // len(seq) if seq else 0

    legacy_result = compute_legacy_score(diagnostics)  # Never used

    # Real aggregation function
    def aggregate_metrics(chain, scores):
        # Extract key components
        valid_scores = [s for s in scores if s > 0]
        chain_length = len(chain)
        avg_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0

        # Secondary metric from chain
        flagged_count = sum(1 for c in chain if c['flagged'])
        adjustment_factor = (chain_length - flagged_count) or 1

        # Tertiary: use of dictionary and zip
        indices = list(range(len(valid_scores)))
        paired_data = dict(zip(indices, valid_scores))
        weighted_sum = sum(i * v for i, v in paired_data.items() if i % 3 == 0)

        # Final computation
        intermediate = (avg_score * adjustment_factor) + weighted_sum
        return int(intermediate * 1.75)  # Deterministic final result

    # Key execution point
    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
    
    # Irrelevant reporting block
    report_summary = {
        'entries': len(processing_chain),
        'valid_diagnostics': len([d for d in diagnostics if d > 5]),
        'checksum': sum(d['aux'] for d in processing_chain) % 1000
    }
    
    # Only this line matters
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()