def main():
    # Sensor calibration constants (some irrelevant)
    base_offset = 17.3
    gain_factor = 0.89
    dummy_threshold = 42.5  # unused red herring

    # Input signal chain
    raw_signals = [3, 7, 12, 18, 25]
    processed = []
    for sig in raw_signals:
        if sig % 2 == 1:
            processed.append(sig ** 2 - base_offset)
        else:
            processed.append(sig + base_offset)

    # Activation filter using lambda (relevant)
    activation_filter = lambda x: x > 20
    filtered = list(filter(activation_filter, processed))

    # Simulate noise injection (partially irrelevant)
    noise_profile = []
    for i in range(5):
        noise_val = (i * 1.7) % 3.1
        noise_profile.append(noise_val)  # Computed but not used

    # Activation chain with conditional amplification
    activation_chain = 0
    temp_cache = []
    for val in filtered:
        if val < 30:
            activation_chain += int(val // gain_factor)
        else:
            temp_cache.append(val * 0.5)  # stored but only sum matters
            activation_chain += int(sum(temp_cache) % 7)

    # Auxiliary debugging trace (distractor logic)
    debug_state = []
    for _ in range(3):
        debug_state.append({'stage': _, 'active': False})  # dead structure

    # Final transformation function
    def final_transform(x):
        # Mix of bitwise and arithmetic ops
        stage1 = (x ^ 105)  # XOR with constant
        stage2 = (stage1 + 37) % 1000
        stage3 = stage2 * gain_factor
        return int(stage3) if stage3 > 50 else int(stage3 * 1.2)

    thermal_output = final_transform(activation_chain)
    
    # Print required result
    print(f"Target result: {thermal_output}")

if __name__ == "__main__":
    main()