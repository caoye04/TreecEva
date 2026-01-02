import itertools

# Simulate multi-stage sensor data processing with interference

def collect_signals(base_freq, harmonics):
    signal_chain = []
    for h in range(1, harmonics + 1):
        value = (base_freq * h) % 17
        if value % 3 == 0:
            signal_chain.append(value * 1.5)
        else:
            signal_chain.append(value ** 1.1)
    return signal_chain


def apply_mask(sequence, key_offset):
    masked = []
    for i, val in enumerate(sequence):
        mask = (i + key_offset) % 5
        if mask > 0:
            masked.append(val / mask)
        else:
            masked.append(val + 1000)  # rare case
    return masked


def filter_anomalies(raw_list):
    # Some values are clearly noise
    threshold = sum(raw_list) / len(raw_list) * 0.5
    cleaned = [x for x in raw_list if x < threshold * 3]
    # Irrelevant transformation
    _ = [x * 0.9 + 2 for x in raw_list if x > 100]  # dead logic
    return cleaned


def generate_synthetic_metadata(size):
    # Distractor: generates unused metadata
    keys = ['M' + str(i % 10) for i in range(size)]
    types = [chr(65 + (i * 3) % 26) for i in range(size)]
    return list(zip(keys, types))


def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * __import__('math').log(p)
    return round(entropy, 6)


def aggregate_features(clean_seq):
    product = 1
    for x in clean_seq[:5]:  # limit to first few
        product *= int(x) % 7
    checksum = product ^ 255  # bit manipulation
    return {
        'magnitude': sum(clean_seq),
        'stability': len([x for x in clean_seq if x < 10]),
        'checksum_flag': checksum,
        'aux_data': generate_synthetic_metadata(50)  # red herring
    }


def finalize_processing(data_blob):
    mag = data_blob['magnitude']
    stab = data_blob['stability']
    flag = data_blob['checksum_flag']
    
    # Complex conditional scoring
    if mag > 50:
        if stab >= 3:
            score = (mag * 0.3) + (stab * 2) - (flag % 10)
        else:
            score = mag * 0.1
    else:
        score = mag * stab
    
    # Misleading secondary computation
    _temp = (mag + stab) // (flag % 9 + 1)
    _unused_result = ''.join([chr((int(mag) + i) % 26 + 97) for i in range(10)])
    
    return int(score)

# Main execution chain
if __name__ == '__main__':
    raw_signal = collect_signals(base_freq=13, harmonics=8)
    processed = apply_mask(raw_signal, key_offset=7)
    filtered = filter_anomalies(processed)
    
    # Dead branch - never taken due to data properties
    if any(x > 1000 for x in filtered):
        fallback = [x / 10 for x in filtered]
    else:
        pass  # implicit continuation

    aggregated_data = aggregate_features(filtered)
    
    # Unused entropy calculation - looks important but isn't
    _entropy = calculate_entropy(filtered)
    
    filtration_score = finalize_processing(aggregated_data)
    print(f"Result: {filtration_score}")