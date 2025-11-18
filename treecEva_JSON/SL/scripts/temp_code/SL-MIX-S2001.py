from functools import reduce
from collections import defaultdict

def preprocess_signal(raw_data):
    return list(map(lambda x: x & 0xFF, raw_data))

def calculate_noise_profile(signal):
    profile = defaultdict(int)
    for i, val in enumerate(signal):
        if i % 3 == 0:
            profile[val] += 1
    return profile

def is_valid_pattern(signal):
    # Short-circuit evaluation is crucial here
    return len(signal) > 10 and sum(signal[:5]) > sum(signal[-5:])

def compute_hash_signature(signal):
    # String hashing component
    signature = ''.join(map(str, signal[:10]))
    return hash(signature) % 1000

def main():
    # Deep space signal data (simulated)
    raw_signal_data = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0, 255, 128, 64, 32, 16, 8, 4, 2, 1, 0]
    
    # Step 1: Preprocess the signal
    processed_signal = preprocess_signal(raw_signal_data)
    
    # Step 2: Check if pattern is valid (short-circuit evaluation)
    if is_valid_pattern(processed_signal) or len(processed_signal) < 5:
        # This branch won't execute due to short-circuit
        validation_score = -1
    else:
        # Step 3: Calculate noise profile
        noise_profile = calculate_noise_profile(processed_signal)
        
        # Step 4: Compute hash signature
        hash_sig = compute_hash_signature(processed_signal)
        
        # Step 5: Calculate validation score using reduce
        validation_components = [
            len(processed_signal),
            sum(noise_profile.values()),
            hash_sig,
            reduce(lambda a, b: a ^ b, processed_signal, 0)  # XOR of all elements
        ]
        
        # Final validation score calculation
        validation_score = reduce(lambda acc, val: acc + (val << 1), validation_components, 0)
    
    print(f"Result: {validation_score}")

if __name__ == "__main__":
    main()