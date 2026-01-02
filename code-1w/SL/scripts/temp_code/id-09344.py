from collections import Counter

# System diagnostic data simulation
diagnostic_logs = ['OK', 'ERROR', 'OK', 'WARNING', 'OK', 'OK', 'ERROR']
log_counts = Counter(diagnostic_logs)

# Identify segments with acceptable status
passed_segments = [status for status in diagnostic_logs if status == 'OK']
failed_count = log_counts['ERROR']
warning_count = log_counts['WARNING']

# Base configuration
base_multiplier = 10
penalty = failed_count * 5 + warning_count * 2

# Critical computation step
final_score = len(passed_segments) * base_multiplier - penalty

print(f"Target result: {final_score}")