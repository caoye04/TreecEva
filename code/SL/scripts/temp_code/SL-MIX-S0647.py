from collections import defaultdict

def transform_tracker(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        return result
    wrapper.call_count = 0
    return wrapper

@transform_tracker
def apply_mask(value, mask):
    return value ^ mask

# Sensor readings from three different sources
readings = [
    [0b11001010, 0b10101010, 0b11110000],
    [0b00110101, 0b01010101, 0b00001111],
    [0b10101010, 0b01010101, 0b11001100]
]

# Bitwise masks for each transformation stage
masks = [0b10101010, 0b01010101, 0b11110000]

processed_signals = 0
valid_readings = defaultdict(int)

for stream_idx in range(len(readings)):
    for reading_idx in range(len(readings[stream_idx])):
        raw_signal = readings[stream_idx][reading_idx]
        masked_signal = apply_mask(raw_signal, masks[reading_idx % len(masks)])
        
        # Only process signals with more than 3 bits set after masking
        if bin(masked_signal).count('1') > 3 and not (raw_signal & 0b1111 == 0):
            processed_signals += masked_signal
            valid_readings[stream_idx] |= (1 << reading_idx)
        elif bin(masked_signal).count('1') <= 3 or (raw_signal & 0b1111 == 0):
            # Apply secondary processing
            secondary_mask = (masked_signal >> 2) & 0b00111100
            if secondary_mask != 0:
                processed_signals ^= secondary_mask

# Final adjustment based on decorator call count
if apply_mask.call_count > 8:
    processed_signals &= 0xFF
else:
    processed_signals |= 0x100

print(f"Result: {processed_signals}")