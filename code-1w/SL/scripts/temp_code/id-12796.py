def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_sum = 0
    for log in logs:
        if 'ERROR' not in log and len(log.strip()) > 0:
            valid_count += 1
            temp_sum += len(log)
    average_length = temp_sum / valid_count if valid_count else 0
    efficiency = (valid_count / total_entries) * 100 if total_entries else 0
    return efficiency, average_length

logs_data = [
    'System initialized',
    'INFO: User login',
    'ERROR: Timeout detected',
    'Data processed successfully',
    'WARNING: High memory usage',
    'Task completed',
    '',
    'INFO: Backup started'
]

# Irrelevant transformation (distractor)
log_stats = [len(log) for log in logs_data if log.strip()]
median_len = sorted(log_stats)[len(log_stats)//2] if log_stats else 0

# Core data processing with mixed logic
productivity = 0
risk_factor = 0
error_count = sum(1 for log in logs_data if 'ERROR' in log)
warning_count = sum(1 for log in logs_data if 'WARNING' in log)
efficiency_rate, avg_log_len = analyze_efficiency(logs_data)

if efficiency_rate > 70:
    productivity += 25
elif efficiency_rate > 50:
    productivity += 15
else:
    productivity += 5

# Bitwise masking for risk level (simulated)
severity_flag = error_count << 2
risk_factor = severity_flag | warning_count

# Use of set operations to filter unique keywords
all_words = []
for log in logs_data:
    if log.strip():
        all_words.extend(log.split())
word_set = set(word.upper() for word in all_words)
info_set = {'INFO', 'SYSTEM', 'USER', 'DATA'}
common_info = word_set & info_set
redundant_chars = ''.join(common_info).count('I')  # semi-relevant distractor

# String-based adjustment
adjustment = len(common_info) * 3.5 if 'SUCCESSFULLY' in word_set else len(common_info) * 2.1
productivity += adjustment

# Final evaluation with logical and bitwise mix
is_optimal = efficiency_rate > 60 and risk_factor < 10
boost = 1.2 if is_optimal else 0.8

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Mock function to finalize score
def evaluate_performance(p, r):
    base = p * boost
    penalty = r * 3.1
    # Additional distraction: unused calculation
    hypothetical = (p ^ r) + median_len  # XOR use as red herring
    return int(base - penalty)

# Print final result as required
Target result: {final_score}