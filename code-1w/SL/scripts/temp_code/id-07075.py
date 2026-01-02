def analyze_system_metrics(data_stream):
    baseline = 42
    temp_cache = []
    checksum = 0
    for val in data_stream:
        if val % 3 == 0 and val % 5 != 0:
            temp_cache.append(val * 0.9)
        elif val % 7 == 0:
            checksum += (val // 2) % 10
    return sum(temp_cache), checksum


def track_iterations(history):
    iteration_map = {i: len(str(hist)) for i, hist in enumerate(history)}
    total_length = sum(iteration_map.values())
    avg_length = total_length / len(iteration_map) if iteration_map else 0
    return total_length, avg_length

# Simulated system logs
event_codes = [15, 21, 33, 49, 55, 63]
execution_trace = [230, 180, 95, 440]

# Irrelevant transformation chain
transformed = list(map(lambda x: x + 10 if x < 100 else x - 5, execution_trace))
filtered = [x for x in transformed if x > 100]
dummy_agg = sum([x ** 0.5 for x in filtered])  # unused aggregation

# Character frequency analysis (semi-relevant)
log_string = "error warn info debug error info warn"
char_freq = {c: log_string.count(c) for c in set(log_string) if c.isalpha()}
alphabet_sum = sum(ord(k) * v for k, v in char_freq.items()) % 1000

# Core state variables
convergence_log = [len(str(code)) for code in event_codes]
efficiency_rating = 85

# Distractor: complex but unused set operation
unique_digits = set()
for num in event_codes:
    unique_digits.update(int(d) for d in str(num))
prime_digits = {2, 3, 5, 7}
disjoint_count = len(unique_digits - prime_digits)

# Helper function using lambda and string methods
validate_entry = lambda s: s.strip().upper().startswith("E")
error_count = sum(1 for word in log_string.split() if validate_entry(word))

# Real computation begins here
size_metric, _ = analyze_system_metrics(execution_trace)
length_total, _ = track_iterations([event_codes, convergence_log])

# Modular arithmetic with character count influence
mod_factor = (alphabet_sum + error_count) % 13
adjusted_efficiency = (efficiency_rating + mod_factor * 2) % 100

# Final evaluation logic
convergence_score = sum(convergence_log) * 3
penalty = 0
if len(convergence_log) >= 4:
    penalty += 10
if adjusted_efficiency < 80:
    penalty += 15

final_score = evaluate_performance(convergence_log, efficiency_rating) if 'evaluate_performance' in globals() else None

def evaluate_performance(log, rating):
    base = sum(log) * 5
    adjustment = rating // 5
    return base + adjustment - penalty

final_score = evaluate_performance(convergence_log, efficiency_rating)
print(f"Target result: {final_score}")