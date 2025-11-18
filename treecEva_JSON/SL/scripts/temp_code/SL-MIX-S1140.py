def calculate_interference(depth, frequency):
    if depth <= 0:
        return frequency & 0xF
    
    sub_signal_1 = calculate_interference(depth - 1, (frequency << 1) ^ 0xAAAA)
    sub_signal_2 = calculate_interference(depth - 1, (frequency >> 1) ^ 0x5555)
    
    combined = (sub_signal_1 ^ sub_signal_2) & 0xFF
    return (combined * 3 + depth) % 97

def process_signals():
    signals = [0x1234, 0x5678, 0x9ABC, 0xDEF0]
    interference_map = {}
    
    for i, sig in enumerate(signals):
        interference_map[i] = calculate_interference(3, sig)
    
    aggregate = 0
    for k, v in interference_map.items():
        if v & 1:
            aggregate ^= (v << k)
        else:
            aggregate += (v >> (k % 3))
    
    return aggregate % 1024

interference_score = process_signals()
print(f"Result: {interference_score}")