def analyze_signal(data, threshold=0.75):
    """ Analyze sensor signal with multiple false paths and distractions """
    import math

    # Irrelevant pre-processing (distractor)
    temp_log = [math.sin(x) for x in data if x > 0.5]
    temp_log = [round(t, 3) for t in temp_log]
    normalization_factor = sum(temp_log) if temp_log else 1.0

    # Real path begins: filter significant amplitudes
    filtered_data = [x for x in data if abs(x) > threshold]

    # Distractor: unused transformation chain
    transformed = []
    for x in data:
        if x < 0:
            transformed.append(abs(x) ** 0.5)
        elif x > 1:
            transformed.append(math.log(x))
        else:
            transformed.append(x * 2)

    # Dead code path: never called function
    def decrypt_phase(signal):
        return [s ^ 5 for s in signal]  # Bitwise red herring

    # Another distraction: character counting in hex representation
    hex_counters = {}
    for val in filtered_data:
        hx = hex(int(abs(val) * 100))[2:]
        for char in hx:
            if char.isalpha():
                hex_counters[char] = hex_counters.get(char, 0) + 1

    # Actual logic disguised among noise: count oscillations
    zero_crossings = 0
    for i in range(1, len(filtered_data)):
        if (filtered_data[i-1] > 0) != (filtered_data[i] > 0):
            zero_crossings += 1

    # Hidden meaningful assignment
    base_score = len(filtered_data) * 2
    adjustment = zero_crossings << 2  # Multiply by 4 using bit shift

    # Decoy result that looks important but isn't used
    diagnostic_checksum = 0
    for i, v in enumerate(filtered_data):
        diagnostic_checksum += int(v) ^ i

    # Critical operation buried in middle
    final_diagnostic = base_score + adjustment - 5

    # More irrelevant output
    stats_summary = {
        'count': len(data),
        'high_freq': len([x for x in data if x > 1.0]),
        'negative_ratio': len([x for x in data if x < 0]) / len(data)
    }

    # String manipulation distractor
    key_tag = 'SIG-{thr}'.format(thr=int(threshold*100))
    tag_parts = key_tag.split('-')
    tag_parts.append('ANALYZED')
    reconstructed_tag = '-'.join(tag_parts).lower()

    # Final red herring: unused bitwise aggregate
    aggregate_flag = 0
    for x in [int(abs(d)*10) % 8 for d in filtered_data]:
        aggregate_flag |= (1 << x)

    return final_diagnostic


def process_readings(readings):
    """ Wrapper that performs secondary analysis """
    if not readings:
        return -1

    # Real contribution: sum of absolute values adjusted by length
    magnitude = sum(abs(r) for r in readings)
    penalty = len(readings) * 0.5

    # Distractor: string-based encoding of readings
    encoded = ''
    for r in readings:
        whole = str(int(abs(r)))
        encoded += ''.join(chr(ord(c) + 1) for c in whole)

    # This looks important but doesn't affect result
    validation_key = ''
    for i, c in enumerate(encoded):
        if i % 2 == 0:
            validation_key += c.lower()
        else:
            validation_key += c.upper()

    # The real computation
    raw_result = magnitude - penalty

    # Final adjustment based on parity of total
    if int(magnitude) & 1:
        raw_result += 2.5
    else:
        raw_result -= 1.5

    return int(raw_result * 2)  # Convert to integer scale

# Main execution
sensor_input = [0.1, -0.3, 0.8, -1.2, 1.5, -0.9, 2.1, 0.4, -1.7, 1.3]
intermediate = analyze_signal(sensor_input, threshold=0.75)
final_diagnostic = process_readings(intermediate)
print(f"Target result: {final_diagnostic}")