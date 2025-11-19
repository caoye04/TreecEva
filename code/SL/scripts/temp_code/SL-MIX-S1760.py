from collections import defaultdict
import itertools

def encode_timestamp(ts):
    encoded = ''
    while ts > 0:
        encoded = chr(ord('A') + ts % 26) + encoded
        ts //= 26
    return encoded if encoded else 'A'

def calculate_frequency(sequence):
    freq_map = defaultdict(int)
    for char in sequence:
        freq_map[char] += 1
    return dict(freq_map)

timestamps = [1000, 2000, 3000, 4000, 5000]
encoded_signals = []

for ts in timestamps:
    encoded_signals.append(encode_timestamp(ts))

composite_signal = ''.join(encoded_counts for encoded_ts in encoded_signals 
                          for encoded_counts in itertools.repeat(encoded_ts, len(encoded_ts)))
frequency_analysis = calculate_frequency(composite_signal)
anomaly_score = 0

for char, count in frequency_analysis.items():
    if ord(char) % 3 == 0:
        anomaly_score += count * 2
    elif ord(char) % 3 == 1:
        anomaly_score += count
    else:
        anomaly_score -= count

print(f"Result: {anomaly_score}")