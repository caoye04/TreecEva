def analyze_sensor_node(node_data, config):
    cumulative_score = 0
    anomaly_count = 0
    temp_buffer = []
    debug_trace = []

    for idx, reading in enumerate(node_data['readings']):
        raw_value = reading['value'] * config['gain'] + config['offset']
        if raw_value < config['noise_floor']:
            debug_trace.append(f'Noisy: {raw_value}')
            continue

        normalized = abs(raw_value) ** 0.5
        if normalized > config['anomaly_threshold']:
            anomaly_count += 1
            temp_buffer.append(normalized * 0.1)
        else:
            temp_buffer.append(normalized)

    aggregated = sum(temp_buffer)
    if anomaly_count > 3:
        aggregated *= 0.75

    secondary_check = 0
    for i, tb in enumerate(temp_buffer):
        if i % 2 == 0 and tb > 5:
            secondary_check += 1

    cumulative_score = int(aggregated) + secondary_check * 2
    return cumulative_score


def extract_metadata(records):
    meta_list = []
    for r in records:
        if 'meta' in r:
            meta_list.append(r['meta'])
    return meta_list


def decode_transmission(signal_seq):
    decoded = []
    shift_key = 3
    for s in signal_seq:
        shifted = ''.join(chr((ord(c) - ord('a') - shift_key) % 26 + ord('a')) for c in s.lower() if c.isalpha())
        decoded.append(shifted)
    return decoded


def validate_checksum(data):
    total = 0
    for d in data:
        if isinstance(d, dict) and 'value' in d:
            total += d['value']
    return total % 17 == 0


def process_readings(dataset, thresholds):
    results = []
    status_flags = []

    for entry in dataset:
        zone_id = entry['zone']
        base_weight = thresholds.get(zone_id, 1.0)
        score = analyze_sensor_node(entry, {'gain': 1.2, 'offset': -0.5, 'noise_floor': 0.1, 'anomaly_threshold': 6.0})
        weighted_score = score * base_weight

        if weighted_score > 40:
            status_flags.append(1)
        else:
            status_flags.append(0)

        results.append({'zone': zone_id, 'score': weighted_score})

    flag_sum = sum(status_flags)
    adjustment_factor = 1.0
    if flag_sum == 0:
        adjustment_factor = 0.5
    elif flag_sum == len(status_flags):
        adjustment_factor = 1.5

    final_sum = sum(r['score'] for r in results) * adjustment_factor
    intermediate_diag = final_sum / (len(results) or 1)

    # Irrelevant transformation chain
    encoded_signals = ['khoor', 'zruog', 'vdqj']
    decoded = decode_transmission(encoded_signals)
    metadata_records = [{'meta': 'cfg_x9'}, {'meta': 'cfg_y2'}]
    extracted_meta = extract_metadata(metadata_records)
    checksum_valid = validate_checksum([{'value': 5}, {'value': 12}, {'value': 4}])

    # Decoy computation with fake diagnostic
    fake_diagnostic = 0
    for d in decoded:
        for c in d:
            fake_diagnostic += ord(c) % 7
    fake_diagnostic = (fake_diagnostic + len(extracted_meta)) % 1000

    # Actual result path
    scaling_constant = 2.3
    stability_offset = len([x for x in status_flags if x == 1]) * 0.1
    final_diagnostic = round(intermediate_diag * scaling_constant + stability_offset, 4)

    # Unused branching
    if final_diagnostic < 0:
        final_diagnostic = 0
    elif final_diagnostic > 1000:
        final_diagnostic = 999.999

    return final_diagnostic

# Main execution block
sensor_network_data = [
    {
        'zone': 'A1',
        'readings': [
            {'value': 5.2}, {'value': 6.1}, {'value': 0.05}, {'value': 7.3},
            {'value': 8.0}, {'value': 5.8}, {'value': 0.02}, {'value': 6.6}
        ]
    },
    {
        'zone': 'B2',
        'readings': [
            {'value': 4.9}, {'value': 0.03}, {'value': 5.5}, {'value': 6.2},
            {'value': 0.01}, {'value': 7.1}, {'value': 5.9}, {'value': 6.3}
        ]
    },
    {
        'zone': 'A1',
        'readings': [
            {'value': 5.1}, {'value': 6.0}, {'value': 0.04}, {'value': 7.2},
            {'value': 7.9}, {'value': 5.7}, {'value': 0.03}, {'value': 6.5}
        ]
    }
]

threshold_map = {
    'A1': 1.15,
    'B2': 0.95
}

filtered_data = list(filter(lambda x: x['zone'] in threshold_map, sensor_network_data))
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")