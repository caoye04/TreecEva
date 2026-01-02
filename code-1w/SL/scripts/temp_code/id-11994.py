def analyze_signal(samples):
    # Irrelevant preprocessing block (dead path)
    if len(samples) == 0:
        return -999  # Dead code, never reached due to input constraints

    # Real computation begins
    normalized = [round(x / max(samples) * 100, 2) for x in samples]
    
    # Distractor: complex-looking but unused transformation
    transformed = []
    for x in normalized:
        if x > 50:
            transformed.append((x ** 0.5) * 2.1)
        else:
            transformed.append(x / 1.8)
    # End of unused transformation

    # Actual relevant logic
    peaks = [i for i in range(1, len(normalized)-1) if normalized[i-1] < normalized[i] > normalized[i+1]]
    peak_values = [normalized[i] for i in peaks]

    # String-based identifier generation (irrelevant but plausible)
    sig_id = 'SIG-' + ''.join([str(int(v))[-1] for v in normalized[:3]]).zfill(3)
    sig_class = sig_id[4:].lstrip('0')  # Further meaningless manipulation

    # Real data: counting and filtering
    high_activity = [v for v in normalized if v >= 75]
    avg_peak = sum(peak_values) / len(peak_values) if peak_values else 0

    # Bit manipulation red herring
    magic_key = 0
    for v in [len(normalized), len(peaks), len(high_activity)]:
        magic_key ^= (v << 2) | (v >> 1)
    magic_key = magic_key & 0xFF  # Truncate to 8 bits – unused later

    # Slicing distraction
    windowed_sums = [sum(normalized[i:i+3]) for i in range(0, len(normalized), 3)]
    max_window = max(windowed_sums) if windowed_sums else 0

    # Core calculation chain (8–12 logic steps)
    base_energy = sum(normalized) / len(normalized)
    volatility = sum(abs(normalized[i] - normalized[i-1]) for i in range(1, len(normalized)))
    stability_score = 100 - (volatility / len(normalized))

    # Conditional adjustment with short-circuit logic
    adjustment = 10 if stability_score > 80 and (len(peaks) == 0 or max_window < 60) else 5

    # Tuple unpacking that looks important
    config_code, threshold, mode_flag = 2048, 77.5, 'adaptive'
    
    # Unused recursive helper (decoy function)
    def integrate_noise(acc, idx):
        if idx >= len(normalized):
            return acc
        return integrate_noise(acc + (normalized[idx] % 3), idx + 1)
    
    # Actual aggregation
    aggregate_score = int(base_energy + stability_score + adjustment)

    # Correction based on string-derived logic (only partially relevant)
    id_digits = [int(c) for c in sig_id if c.isdigit()]
    digit_sum = sum(id_digits)
    correction_factor = digit_sum if digit_sum % 2 == 0 else -digit_sum

    # Key statement
    final_diagnostic = aggregate_score + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Return nothing; only side effect is printing
    return None

# Input data crafted to yield deterministic result
input_samples = [12.5, 30.0, 95.2, 44.8, 10.1, 96.7, 67.3, 22.0]
analyze_signal(input_samples)