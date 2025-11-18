class AudioNode:
    def __init__(self, sample=0, next_node=None):
        self.sample = sample
        self.next = next_node

def create_signal_chain(samples):
    head = None
    for sample in reversed(samples):
        head = AudioNode(sample, head)
    return head

def process_audio_chain(chain_head, key):
    current = chain_head
    processed_samples = []
    while current:
        # Apply XOR encryption with key
        encrypted = current.sample ^ key
        # Right shift by 2 bits
        shifted = encrypted >> 2
        # Multiply by 3 and add 5
        transformed = shifted * 3 + 5
        processed_samples.append(transformed)
        current = current.next
    return processed_samples

def calculate_final_output(processed_samples):
    # Calculate sum using list comprehension
    squared_values = [x**2 for x in processed_samples]
    # Sum all squared values
    total = sum(squared_values)
    # Bitwise AND with mask 0xFF
    masked = total & 0xFF
    # Final calculation
    return (masked << 1) + 0b101010

# Initialize audio samples as array
audio_samples = [100, 150, 200, 250]

# Create linked list from array
signal_chain = create_signal_chain(audio_samples)

# Process with encryption key
encryption_key = 0b11001100
processed_data = process_audio_chain(signal_chain, encryption_key)

# Calculate final output
final_output = calculate_final_output(processed_data)
print(f"Result: {final_output}")