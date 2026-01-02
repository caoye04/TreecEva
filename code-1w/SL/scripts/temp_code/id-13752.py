def analyze_trend(data, base):
    trend = 0
    adjustments = []
    for i in range(len(data)):
        if data[i] > base:
            trend += 1
            adjustments.append(data[i] - base)
        elif data[i] < base:
            trend -= 1
            adjustments.append(base - data[i])
    net_adjustment = sum(adjustments) / len(adjustments) if adjustments else 0
    return trend, net_adjustment

status_flags = ['active', 'inactive', 'pending', 'active']
data_stream = [12, 15, 10, 18, 14]
base_reference = 13

# Irrelevant string processing (distractor)
user_input = "  Performance Report Q3  "
formatted_title = user_input.strip().replace(' ', '_').lower()
log_entry = f"log_{formatted_title}.txt"

# Simulate system metrics with mixed data types
metrics = [
    ('response_time', 14.2),
    ('throughput', 987),
    ('error_rate', 0.03),
    ('uptime', 99.7)
]

# Extract numeric values using slicing and tuple unpacking
numeric_values = [val for _, val in metrics[1:3]]  # throughput and error_rate only

# Misleading computation path (dead logic)
avg_metric = sum(numeric_values) / len(numeric_values)
scaled_avg = avg_metric * 1.5 if avg_metric > 500 else avg_metric * 0.8

# Core logic hidden among distractions
threshold = 1.0

# Another distraction: unused loop over status flags
activation_count = 0
for flag in status_flags:
    if flag == 'active':
        activation_count += 1

# Real processing begins here
raw_trend, adjustment = analyze_trend(data_stream, base_reference)

# Use string slicing to determine multiplier (key trick)
secret_code = "x7k9p2m"
multiplier_str = secret_code[1:4]  # '7k9'
actual_multiplier = int(multiplier_str[0]) if multiplier_str[0].isdigit() else 1  # uses '7'

# Final decision logic with conditional override
if raw_trend >= 2:
    performance_bonus = 50
else:
    performance_bonus = 20

# Critical assignment
final_score = (raw_trend * actual_multiplier) + performance_bonus

# Print result as required
print(f"Result: {final_score}")