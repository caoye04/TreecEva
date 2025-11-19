from enum import Enum

class DecoderState(Enum):
    INIT = 0
    PROCESSING = 1
    TRANSFORM = 2
    FINALIZE = 3

def decode_signal_sequence(signal_data):
    state = DecoderState.INIT
    accumulator_checksum = 0
    index = 0
    
    while index < len(signal_data):
        if state == DecoderState.INIT:
            # Initialize with first value XORed with 0xFF
            accumulator_checksum = signal_data[index] ^ 0xFF
            index += 1
            state = DecoderState.PROCESSING
        elif state == DecoderState.PROCESSING:
            # Process next 3 values with bitwise AND and shift operations
            if index + 2 < len(signal_data):
                val1 = signal_data[index]
                val2 = signal_data[index+1]
                val3 = signal_data[index+2]
                # Complex bitwise operation chain
                temp_result = ((val1 & val2) << 2) | (val3 >> 1)
                accumulator_checksum ^= temp_result
                index += 3
                state = DecoderState.TRANSFORM
            else:
                # If not enough values, move to finalize
                state = DecoderState.FINALIZE
        elif state == DecoderState.TRANSFORM:
            # Apply arithmetic transformation
            if accumulator_checksum % 5 == 0:
                accumulator_checksum = (accumulator_checksum * 3) + 7
            else:
                accumulator_checksum = (accumulator_checksum // 2) - 3
            state = DecoderState.PROCESSING
        elif state == DecoderState.FINALIZE:
            # Final adjustment with bitwise NOT and masking
            accumulator_checksum = (~accumulator_checksum) & 0xFFFF
            break
    
    return accumulator_checksum

# Encoded signal sequence for processing
encoded_signals = [42, 18, 73, 29, 55, 16, 84, 37]

# Execute the decoding process
final_checksum = decode_signal_sequence(encoded_signals)
print(f"Result: {final_checksum}")