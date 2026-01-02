from collections import defaultdict, Counter

# Simulated system log analysis with performance metrics
def analyze_log_chunk(chunk, filters):
    severity_count = defaultdict(int)
    event_types = []
    temp_accumulator = 0

    for line in chunk:
        parts = line.split('|')
        if len(parts) < 3:
            continue
        level, code, msg = parts[0].strip(), parts[1].strip(), parts[2].strip()

        # Irrelevant filtering (distractor)
        if code in filters.get('ignore', []):
            continue

        severity_count[level] += 1
        event_types.append(code)

        # Real computation buried in noise
        if level == 'CRITICAL' and 'timeout' in msg:
            temp_accumulator += 3
        elif level == 'ERROR' and 'retry' in msg:
            temp_accumulator += 1

    # Dead return path — never used in final logic
    type_freq = Counter(event_types)
    return dict(severity_count), temp_accumulator, type_freq


def compute_baseline(reference_window):
    # Complex but irrelevant baseline calculation
    base = sum([len(ref) for ref in reference_window]) // len(reference_window)
    adjustment = 0
    for i, ref in enumerate(reference_window):
        if i % 2 == 0:
            adjustment += len(ref) * 0.1
    return int(base + adjustment)


def extract_signals(raw_logs):
    # Signal extraction with red herring operations
    signals = []
    buffer = []
    for log in raw_logs:
        words = log.split()
        for word in words:
            if word.isnumeric() and int(word) > 1000:
                buffer.append(int(word))
    # This is a decoy aggregation
    decoy_metric = sum(buffer) // len(buffer) if buffer else 0

    # Real signal: count occurrences of 'ACK'
    ack_count = sum(1 for log in raw_logs if 'ACK' in log)
    signals.append(('ack_packets', ack_count))

    # Fake complexity: unused transformation
    transformed = [x ^ 7 for x in buffer[:5]]

    signals.append(('decoy_value', decoy_metric))
    return signals


def aggregate_performance(log_entries, thresholds):
    # Core logic hidden among distractions
    total_weight = 0
    penalty = 0
    bonus = 0

    # Key data structures
    level_freq = defaultdict(int)
    sequence_gaps = []

    # Real processing
    indices = []
    for i, entry in enumerate(log_entries):
        if 'SEQ' in entry:
            try:
                seq_num = int(entry.split('SEQ')[1].split()[0])
                indices.append(seq_num)
            except:
                pass

        # Count severity levels (relevant)
        if 'WARNING' in entry:
            level_freq['WARNING'] += 1
        if 'ERROR' in entry or 'CRITICAL' in entry:
            level_freq['ERROR'] += 1

    # Critical logic: gap detection in sequence numbers
    for i in range(1, len(indices)):
        if indices[i] - indices[i-1] > 1:
            sequence_gaps.append(indices[i] - indices[i-1] - 1)

    # Main scoring mechanism
    missing_packets = sum(sequence_gaps)
    total_weight += len(indices)  # reward valid sequences
    penalty += missing_packets * 5
    penalty += level_freq['ERROR'] * 3
    bonus += level_freq['WARNING'] // 2  # minor compensation

    # Distractor: complex unused calculation
    history = [abs(a - b) for a, b in zip(indices, indices[1:])]    
    smoothed = sum(history[i] * 0.9**i for i in range(len(history))) if history else 0.0

    # Another red herring: timestamp emulation
    timestamps = [i * 17 % 1003 for i in range(len(log_entries) // 10)]
    avg_gap = sum(abs(timestamps[i] - timestamps[i-1]) for i in range(1, len(timestamps))) / len(timestamps) if timestamps else 0

    # Final score depends only on key reasoning path
    final_score = total_weight - penalty + bonus

    # Irrelevant normalization
    if final_score > 0:
        final_score = int(final_score * (1 + 0.1 * (smoothed // 10)))

    return final_score

# Input data
log_stream = [
    'INFO|NET|Connection established',
    'WARNING|IO|Disk latency high',
    'INFO|NET|Heartbeat ACK',
    'CRITICAL|SYS|System timeout detected SEQ10',
    'ERROR|NET|Packet loss, retrying SEQ11',
    'INFO|NET|Data sent',
    'INFO|CTRL|Sequence update',
    'WARNING|NET|Unusual ACK pattern',
    'INFO|NET|ACK received SEQ14',
    'INFO|MON|Resource check OK',
    'ERROR|STORAGE|Write failed SEQ15',
    'INFO|NET|ACK received SEQ17',  # gap of 1 missing
    'WARNING|NET|Latency fluctuation',
    'INFO|NET|ACK received SEQ20',  # gap of 2 missing
]

thresholds = {
    'critical_limit': 5,
    'ignore': ['DBG', 'TRACE'],
    'window_size': 3
}

# Execution point of interest
final_score = aggregate_performance(log_stream, thresholds)
print(f"Result: {final_score}")