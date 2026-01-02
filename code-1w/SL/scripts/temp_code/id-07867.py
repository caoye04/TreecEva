from collections import Counter
import itertools

# Simulated network packet analysis with red herrings
def analyze_traffic(packets):
    stats = Counter()
    temporal_gaps = []
    decoy_sum = 0
    fake_threshold = 0
    phase_shift = 0

    for pkt in packets:
        length = len(pkt['data'])
        timestamp = pkt['ts']
        stats['total_packets'] += 1
        stats['total_bytes'] += length

        # Irrelevant frequency analysis (distractor)
        freq_map = {}
        for c in pkt['data']:
            if c.isalpha():
                freq_map[c.lower()] = freq_map.get(c.lower(), 0) + 1
        sorted_freq = sorted(freq_map.items(), key=lambda x: -x[1])
        if sorted_freq:
            decoy_sum += ord(sorted_freq[0][0])

        # Real gap tracking (used later)
        if len(temporal_gaps) > 0:
            gap = timestamp - temporal_gaps[-1]
            temporal_gaps.append(timestamp)
            if gap > 500:
                stats['large_gaps'] += 1
        else:
            temporal_gaps.append(timestamp)

        # Fake entropy calculation (dead path)
        char_counts = [count for _, count in freq_map.items()]
        total = sum(char_counts)
        if total > 0:
            entropy = 0
            for count in char_counts:
                p = count / total
                entropy -= p * __import__('math').log2(p + 1e-9)
            phase_shift += int(entropy * 10) % 7

    # Misleading normalization (unused)
    if stats['total_packets'] > 0:
        normalized_load = (stats['total_bytes'] / stats['total_packets']) * 0.87
        adjustment_factor = min(normalized_load / 100, 1.5)
        fake_threshold = int(adjustment_factor * 42)

    # Real logic begins: find sequences with repeating patterns
    data_stream = ''.join([p['data'] for p in packets])
    pattern_counter = Counter()
    for i in range(len(data_stream) - 4):
        substr = data_stream[i:i+5]
        if substr.isalnum() and len(set(substr)) < 3:
            pattern_counter[substr] += 1

    valid_patterns = [p for p, cnt in pattern_counter.items() if cnt >= 2]
    valid_count = len(valid_patterns)

    # Secondary validation using character transitions (partially relevant)
    transitions = []
    for s in valid_patterns:
        for j in range(len(s) - 1):
            transitions.append((s[j], s[j+1]))
    transition_freq = Counter(transitions)
    consistency_score = sum(1 for t, c in transition_freq.items() if c >= 2)

    # Key derivation from time gaps (critical path)
    avg_gap = sum(abs(temporal_gaps[i] - temporal_gaps[i-1]) for i in range(1, len(temporal_gaps)))
    if len(temporal_gaps) > 1:
        base_key = int(avg_gap / len(temporal_gaps))
    else:
        base_key = 1

    # Bit manipulation chain (key step)
    extended_key = base_key << 3
    masked_key = extended_key & 0xFF00
    inverted_key = (~masked_key) & 0xFFFF
    shifted_key = (inverted_key >> 4) | (inverted_key << 12)

    # Final checksum computation (TARGET STATEMENT)
    checksum = (valid_count * 31) ^ (shifted_key & 0xFFFF)

    # Decoy output printing (irrelevant)
    debug_info = {
        'decoy_sum': decoy_sum,
        'phase_shift': phase_shift,
        'fake_threshold': fake_threshold,
        'consistency_score': consistency_score
    }

    # ONLY this line matters for the answer
    print(f"Result: {checksum}")

# Setup test data
test_packets = [
    {'ts': 1000, 'data': 'AAAAA'},
    {'ts': 1600, 'data': 'BBBBB'},
    {'ts': 2300, 'data': 'CCCCC'},
    {'ts': 3100, 'data': 'AAAAA'},
    {'ts': 4000, 'data': 'BBBBB'},
    {'ts': 5000, 'data': 'DDDDD'},
    {'ts': 6100, 'data': 'EEEEF'},
    {'ts': 7300, 'data': 'FFFFF'}
]

# Execute
analyze_traffic(test_packets)