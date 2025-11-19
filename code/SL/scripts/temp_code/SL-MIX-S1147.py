from collections import defaultdict

def compute_signal_parity(raw_signals):
    parity_accumulator = 0
    for signal in raw_signals:
        parity_accumulator ^= signal
    return parity_accumulator

# Simulate incoming sensor data
sensor_readings = [0b1101001, 0b1010110, 0b0110110]
parity_mask = 0b1111111

# Process signals through parity checker
processed_signals = list(map(lambda x: x & parity_mask, sensor_readings))
signal_counter = defaultdict(int)
for sig in processed_signals:
    signal_counter[sig] += 1

unique_signals = list(signal_counter.keys())
parity_result = compute_signal_parity(unique_signals)

# Apply final correction using bitwise operations
parity_check = (parity_result >> 1) ^ (parity_result & 0b1111)
print(f"Result: {parity_check}")