from itertools import cycle, islice

def main():
    # Real data pipeline for encoding sensor readings
    raw_readings = [234, 567, 891, 123, 456, 789]
    calibration_factor = 0.987
    normalized = [x * calibration_factor for x in raw_readings]
    
    # Irrelevant transformation chain (distractor)
    shadow_buffer = [x ** 0.5 for x in raw_readings if x > 300]
    shadow_buffer = [x + 10 for x in shadow_buffer]
    temp_shadow = sum(shadow_buffer) // len(shadow_buffer) if shadow_buffer else 0

    # Key processing: filter and quantize
    filtered = [int(x) for x in normalized if x > 400]
    shifted = [x >> 2 for x in filtered]  # Bit manipulation

    # Decoy statistical analysis (dead path)
    mean_val = sum(filtered) / len(filtered) if filtered else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in filtered) / len(filtered) if filtered else 0
    entropy_dust = variance_proxy * 0.123

    # Actual signal extraction via XOR folding
    folded = 0
    for val in shifted:
        folded ^= val
        folded = (folded << 1) & 0xFFFF  # Rotate left behavior
    
    # Salt generation with red herring logic
    decoy_keys = {f'k{i}': (i * 97) % 251 for i in range(10)}
    salt_seed = sum(decoy_keys[k] for k in decoy_keys if '5' in k)  # Only k5 triggers
    salt = (salt_seed ^ 0xABCD) & 0xFF

    # Processed stream is used in final step
    processed = (folded ^ salt) & 0xFFFF

    # Distractor: unused recursive function
    def recurse_noise(n):
        if n < 2:
            return n
        return recurse_noise(n-1) + recurse_noise(n-2)
    
    ignore_result = recurse_noise(6)  # Fibonacci(6)=8, irrelevant

    # Final checksum computation (target)
    def finalizer(value, salt):
        return (value + salt * 3) ^ 0x55AA

    checksum = finalizer(processed, salt)

    # Unrelated list comprehension cleanup
    cleanup = [x for x in [1, 2, 3] for _ in range(2)]
    alt_checksum = sum(cycle([1, 2]))  # Infinite iterator misuse, not executed

    # Output target result
    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()