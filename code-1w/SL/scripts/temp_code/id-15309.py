from collections import defaultdict, Counter
import itertools

# Simulated sensor network data processing with red herrings
def collect_diagnostics():
    raw_readings = [14, 7, 22, 9, 14, 8, 22, 11, 7, 9, 14, 25]
    calibration_sequence = [3, 1, 4, 1, 5]  # Unused in final logic
    baseline_offset = 6  # Distractor: looks important but not used
    mode_frequencies = Counter(raw_readings)

    # Irrelevant transformation chain
    transformed = [x ** 2 % 17 for x in raw_readings]
    shifted = [y + 5 for y in transformed if y < 12]
    aggregated = sum(shifted) // len(shifted) if shifted else 0  # Dead-end calculation

    # Actual signal filtering based on frequency and thresholds
    frequent_values = [val for val, cnt in mode_frequencies.items() if cnt >= 2]
    adjusted_readings = [x - 1 for x in raw_readings]  # Core preprocessing step

    # Decoy statistical analysis (never called)
    def analyze_entropy(data):
        counts = Counter(data)
        total = len(data)
        return sum(-(cnt/total)*((cnt/total).__log__() for cnt in counts.values()))

    # Real processing begins here
    filtered_data = []
    for val in adjusted_readings:
        if val in frequent_values and val % 2 == 1:
            filtered_data.append(val)
    filtered_data = list(dict.fromkeys(filtered_data))  # Remove duplicates preserving order

    # Complex threshold map with irrelevant entries
    threshold_map = defaultdict(lambda: 100)
    threshold_map.update({
        6: 12, 10: 8, 13: 20, 21: 5,  # Only 13:20 is relevant
        'dummy_key_1': 999, 'meta_threshold': 42  # Obvious distractors
    })

    # Unused recursive helper (red herring)
    def recursive_sum(n):
        return n + recursive_sum(n-1) if n > 0 else 0

    # Bit manipulation decoy
    checksum = 0
    for x in raw_readings[:5]:
        checksum ^= x << 1
        checksum &= 0xFF

    # Key control flow with misleading branches
    safety_lock = True
    override_code = "".join([chr(97 + (i*2)%26) for i in range(8)])  # generates non-matching string

    if safety_lock and any(ord(c) > 100 for c in override_code):  # False condition
        recovery_mode = [x * 3 for x in raw_readings]
    elif len(filtered_data) > 3 and not safety_lock:  # Also false
        recovery_mode = [x + 100 for x in filtered_data]
    else:
        # This branch contains actual computation
        magnitude_factor = sum(frequent_values) // len(frequent_values) if frequent_values else 0
        normalized = [x * magnitude_factor for x in filtered_data]
        
        # Final processing function defined inline to obscure flow
        def process_readings(data_list, thresholds):
            result = 0
            for idx, item in enumerate(data_list):
                adjustment = thresholds.get(13, 5)  # Uses default 5 when 13 not found
                if idx % 2 == 0:
                    result += item * adjustment
                else:
                    result -= item
            return result + 3  # Final offset
        
        final_diagnostic = process_readings(filtered_data, threshold_map)
        
        # Multiple print statements to obscure output
        debug_info = {"raw": len(raw_readings), "filtered": len(filtered_data), "check": aggregated}
        log_entry = f"Diagnostics complete: {final_diagnostic} (ref={aggregated})"
        
        # Critical: this is the only required output
        return final_diagnostic

result_value = collect_diagnostics()
print(f"Target result: {result_value}")