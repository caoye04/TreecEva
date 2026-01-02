import math

# Simulated sensor array data processing with diagnostic evaluation
def main():
    raw_signals = [5, 8, 12, 14, 7, 6, 13, 11, 9, 10]
    calibration_offset = 3
    sample_window = 4
    noise_floor = 1.5
    max_amplitude = 16
    temporal_weight = 0.85

    # Irrelevant auxiliary constants (distractors)
    debug_mode = False
    log_buffer_size = 2048
    timestamp_resolution = 'ms'
    system_uptime = 1274
    dummy_flag = True

    # Initial transformation - apply exponential smoothing
    smoothed = []
    for i in range(len(raw_signals)):
        weight = temporal_weight ** (len(raw_signals) - i - 1)
        smoothed.append(raw_signals[i] * weight)

    # Normalize and shift using calibration offset
    normalized = [(x - calibration_offset) / max_amplitude for x in smoothed]

    # Apply moving average filter
    filtered = []
    for i in range(len(normalized)):
        start = max(0, i - sample_window + 1)
        window_avg = sum(normalized[start:i+1]) / (i - start + 1)
        filtered.append(window_avg)

    # Amplify weak signals above noise floor
    amplified = []
    for val in filtered:
        if abs(val) > noise_floor:
            amplified.append(val * 1.5)
        else:
            amplified.append(val * 1.1)  # minor boost

    # Decoy computation: frequency domain analysis (unused)
    def fourier_approx(arr):
        real = [0] * len(arr)
        for k in range(len(arr)):
            for n in range(len(arr)):
                angle = 2 * math.pi * k * n / len(arr)
                real[k] += arr[n] * math.cos(angle)
        return [x / len(arr) for x in real]

    frequency_components = fourier_approx(amplified)  # dead end
    spectral_entropy = 0
    for comp in frequency_components:
        if comp != 0:
            spectral_entropy -= comp * math.log(abs(comp))

    # Actual signal processing path
    processed_data = []
    for x in amplified:
        if x > 0:
            processed_data.append(math.log(x + 1) * 100)
        else:
            processed_data.append(math.exp(x) * 50)

    # Bit manipulation red herring
    checksum = 0
    for val in raw_signals:
        checksum ^= int(val * 10) << 1
        checksum &= 0xFFFF
        checksum = ((checksum >> 15) | (checksum << 1)) & 0xFFFF  # rotate

    metadata_mask = 0xA3D1
    masked_checksum = checksum ^ metadata_mask  # unused result

    # Higher-order function for threshold logic
    threshold_func = lambda x: x > 45 and x < 95

    # Decoy state machine (never executed)
    class StateEngine:
        def __init__(self):
            self.state = 'IDLE'
            self.buffer = []

        def transition(self, val):
            if self.state == 'IDLE' and val > 70:
                self.state = 'ACTIVE'
            elif self.state == 'ACTIVE' and val < 30:
                self.state = 'COOLDOWN'

    engine = StateEngine()  # instantiated but not used

    # Core diagnostic analysis
    def analyze_readings(data, predicate):
        count_valid = 0
        sum_critical = 0.0
        peak = -float('inf')
        history = []

        for reading in data:
            # Nested conditional filtering
            if reading > 10:
                history.append(reading)
                if len(history) >= 3 and history[-1] > history[-2] > history[-3]:
                    reading *= 1.2  # trend amplification

            if predicate(reading):
                count_valid += 1
                sum_critical += reading
                if reading > peak:
                    peak = reading

        # Complex aggregation with fallback logic
        if count_valid == 0:
            return max(data) if data else 0
        
        avg_critical = sum_critical / count_valid
        penalty = 0
        
        # Spurious branching with unused variables
        if len(data) > 5:
            deviation = sum(abs(x - avg_critical) for x in data) / len(data)
            if deviation > 20:
                anomaly_score = deviation * 1.8
                correction_factor = 0.9
            else:
                anomaly_score = 0
                correction_factor = 1.0
            penalty = int(anomaly_score / 5)

        base_result = int(avg_critical) - penalty

        # Final adjustment using bitwise trick (actually relevant)
        final_shift = base_result >> 2
        adjusted = base_result - final_shift

        # Dead code: historical comparison (unreachable)
        def get_baseline_reference():
            return [40, 55, 60, 50, 45]
        
        if False:  # unreachable block
            baseline = get_baseline_reference()
            adjusted = max(adjusted, sum(baseline) / len(baseline))

        return adjusted

    final_diagnostic = analyze_readings(processed_data, threshold_func)
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()