def analyze_sensor_data(raw_readings, threshold_multiplier=1.75):
    # Irrelevant preprocessing: normalize data (not used in final result)
    normalized = [x * 0.98 for x in raw_readings if x > 0]
    filtered = [x for x in raw_readings if x >= sum(raw_readings) / len(raw_readings)]

    # Distractor: complex but unused transformation chain
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 2 == 0:
            transformed.append(val ** 0.5 * (i + 1))
        else:
            transformed.append(val * 1.1)

    # Real computation begins: extract quality flags using bitwise logic
    quality_flags = []
    for reading in raw_readings:
        flag = 0
        flag |= (reading & 1) << 3           # LSB indicates oddness
        flag |= ((reading >> 2) & 1) << 2      # Bit 2 reflects bit 2 state
        flag |= (1 if reading > 50 else 0)   # High reading indicator
        quality_flags.append(flag)
    
    # Misleading diagnostic path (dead end)
    baseline_risk = sum(1 for f in quality_flags if f > 5) * 0.3
    risk_profile = [baseline_risk * (i + 1) for i in range(5)]  # Unused

    # Actual signal extraction: find stable segments
    stable_segments = []
    for i in range(len(raw_readings) - 2):
        if abs(raw_readings[i] - raw_readings[i+1]) < 5 and abs(raw_readings[i+1] - raw_readings[i+2]) < 5:
            stability_score = (raw_readings[i] + raw_readings[i+1] + raw_readings[i+2]) // 3
            stable_segments.append(stability_score)
    
    # Distractor: zip with unrelated index tracking
    indexed_flags = list(zip(range(len(quality_flags)), quality_flags))
    flag_summary = sum(f for _, f in indexed_flags if _ % 3 == 0)

    # Critical path: construct processing chain using enumerate
    processing_chain = []
    for idx, segment in enumerate(stable_segments):
        if idx % 2 == 0:
            processed = segment ^ (idx + 3)  # XOR perturbation
        else:
            processed = segment + (flag_summary % 4)
        processing_chain.append(processed)

    # Decoy aggregation (never called)
    def legacy_aggregate(seq):
        return sum(x * 0.8 for x in seq if x > 40)

    # Real aggregation function defined inside to obscure flow
    def aggregate_metrics(chain, key):
        base = sum(chain)
        adjustment = 0
        for i, val in enumerate(chain):
            if i < key:
                adjustment += val % (i + 2)
        return base - adjustment

    # Validation key derived from bit count in initial readings
    bit_population = sum(bin(x).count('1') for x in raw_readings[:4])
    validation_key = bit_population % 7

    # Final computation - target statement
    final_diagnostic = aggregate_metrics(processing_chain, validation_key)

    # Red herring: alternative metric that looks important
    composite_index = (sum(transformed) / 100) * validation_key if transformed else 0

    # Output the required result
    print(f"Result: {final_diagnostic}")

# Simulate sensor input (deterministic)
sensor_input = [62, 48, 51, 55, 49, 63, 61, 52]
analyze_sensor_data(sensor_input)