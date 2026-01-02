from itertools import compress, count

def main():
    # Simulate sensor data stream with timestamps
    raw_readings = [23.5, 24.1, 25.3, 26.0, 25.8, 25.0, 24.5, 24.2, 24.8, 25.1]
    base_timestamps = list(range(1000, 1010))

    # Irrelevant transformation: scale for no real purpose
    scaled_values = [round(x * 1.017, 3) for x in raw_readings]
    derived_flags = [1 if x > 25.0 else 0 for x in raw_readings]

    # Misleading intermediate calculation (not used in final result)
    phantom_integral = sum(scaled_values[i] * (i+1) for i in range(len(scaled_values)))
    normalization_factor = max(scaled_values) - min(scaled_values)

    # Create paired data with auxiliary metadata
    flow_data = list(zip(count(1), raw_readings, base_timestamps, ["A","B","C","D","E","F","G","H","I","J"] ))

    # Red herring: complex filter that isn't actually used
    def temporal_outlier(seq, window=3):
        result = []
        for i in range(len(seq)):
            window_start = max(0, i - window)
            neighbors = seq[window_start:i + window + 1]
            avg = sum(neighbors) / len(neighbors)
            if abs(seq[i] - avg) > 0.8:
                result.append(i)
        return result

    outliers = temporal_outlier(raw_readings)

    # Real logic begins: threshold function based on dynamic condition
    def threshold_func(entry):
        index, temp, ts, label = entry
        if index % 2 == 0:
            return temp > 24.5
        else:
            return temp > 24.0 and ts % 2 == 0

    # Core calculation with distractor variables inside
    def calculate_equilibrium(data, condition):
        counter = 0
        cumulative = 0
        debug_states = []  # Collected but not used

        for item in data:
            idx, value, timestamp, tag = item

            # Distractor: complex unpacking and unused state tracking
            meta_state = (idx + timestamp) % 4
            debug_states.append(meta_state)

            # Actual decision logic
            if condition(item):
                cumulative += value * idx
                counter += 1

                # Early break based on irrelevant heuristic
                if counter > 0 and cumulative > 100:
                    break

        # Final computation using only relevant accumulated values
        if counter == 0:
            return 0
        
        # Introduce modular arithmetic twist
        mod_adjusted = int(cumulative) % 97
        return (mod_adjusted * 2) - counter  # Key formula

    # Execution point of interest
    equilibrium_score = calculate_equilibrium(flow_data, threshold_func)

    # Unrelated post-processing (dead code path)
    secondary_analysis = [x for x in scaled_values if x < 25.0]
    if len(secondary_analysis) > 3:
        adjustment = sum(secondary_analysis[:3]) / 3
    else:
        adjustment = 0

    # Output required variable
    print(f"Result: {equilibrium_score}")

if __name__ == "__main__":
    main()