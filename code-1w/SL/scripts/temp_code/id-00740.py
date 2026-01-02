def analyze_signal(strength, threshold=0.6):
    return 'strong' if strength > threshold else 'weak'


def encode_status(signal_str, mode='hex'):
    if mode == 'hex':
        return hex(hash(signal_str) % 10000)
    return bin(hash(signal_str) % 10000)

# Irrelevant helper function (dead code path)
def deprecated_calibrate(values):
    adjusted = [v * 0.95 for v in values if v > 10]
    return sum(adjusted) // len(adjusted) if adjusted else 0

# Unused transformation chain
text_buffer = "temp_log_2024"
buffer_upper = text_buffer.upper()
buffer_clean = buffer_upper.replace("TEMP", "CACHE")
encoded_tag = encode_status(buffer_clean, 'bin')

# Core data structures
log_data = [
    {"id": 101, "val": 85, "flag": True},
    {"id": 102, "val": 42, "flag": False},
    {"id": 103, "val": 73, "flag": True},
    {"id": 104, "val": 55, "flag": False}
]

system_state = {
    "active": True,
    "mode": "diagnostic",
    "cache_level": 77,
    "overclock": False,
    "checksum": 0xDEADBEEF
}

# Distractor: unused intermediate calculations
baseline = sum(entry["val"] for entry in log_data) / len(log_data)
offset_correction = int(baseline * 0.05) if baseline > 60 else int(baseline * 0.03)

# Simulated signal analysis (partially relevant)
signals = [0.45, 0.72, 0.33, 0.81]
analyzed = [analyze_signal(s) for s in signals]
dominant = 'strong' if analyzed.count('strong') >= 2 else 'weak'

# Real computation begins here
filtered_values = [e["val"] for e in log_data if e["flag"]]
sum_filtered = sum(filtered_values)

# Bit manipulation red herring
magic_seed = 0xCAFEBABE
scrambled = sum_filtered ^ (magic_seed & 0xFFFF)
descrambled = scrambled ^ (magic_seed & 0xFFFF)  # Reversal (net zero effect)

# Conditional expression with distractor branch
critical_mode = system_state["overclock"] or system_state["cache_level"] > 75
adjustment_factor = 1.25 if critical_mode else 0.85

# Key transformation chain
intermediate_score = descrambled * adjustment_factor

# Additional irrelevant string processing
diag_label = "System Final Diagnostic"
label_lower = diag_label.lower()
char_count = len(label_lower.replace(" ", ""))
vowel_count = sum(1 for c in label_lower if c in 'aeiou')

# Main metric calculation
raw_metric = int(intermediate_score)
penalty = 10 if 'weak' in analyzed else 0
adjusted_metric = raw_metric - penalty

# Final logic with conditional expression and nesting
if system_state["active"]:
    if system_state["mode"] == "diagnostic":
        safety_override = False
        if dominant == 'strong':
            safety_override = True
        
        temp_result = adjusted_metric + (25 if safety_override else -15)
        
        # Nested bitwise check with misleading comment
        # NOTE: This simulates error correction but only triggers in edge cases
        error_flag = (temp_result & 7) == 0  # Rare condition
        final_adjust = temp_result ^ 8 if error_flag else temp_result | 4
        
        # Final aggregation
        aux_data = [system_state["cache_level"], sum_filtered, len(log_data)]
        avg_aux = sum(aux_data) / len(aux_data)
        deviation = abs(final_adjust - avg_aux)
        
        # Actual answer computation
        stability_index = final_adjust - int(deviation * 0.5)
        
        # Redundant validation layer (distractor)
        validation_sum = sum(
            1 for x in [stability_index, avg_aux, baseline]
            if x > 50
        )
        
        # Critical assignment
        final_diagnostic = stability_index + validation_sum
    else:
        final_diagnostic = -999  # Dead branch
else:
    final_diagnostic = 0  # Dead branch

Result: {final_diagnostic}