def analyze_efficiency(metrics):
    efficiency_list = [m * 1.5 for m in metrics if m > 20]
    adjusted = sum(efficiency_list) / len(metrics)
    return adjusted

metrics_data = [15, 25, 30, 40, 10]
baseline = sum(m for m in metrics_data if m < 25)
dummy_calc = baseline * 0.1

productivity = analyze_efficiency(metrics_data)

status_flags = {"high": 3, "medium": 2, "low": 1}
risk_set = {"high", "medium"}
flag_values = set(status_flags.keys())
overlap = risk_set & flag_values
risk_factor = len(overlap) * 1.5

# Irrelevant string transformation chain
raw_code = "AbC"
converted = raw_code.lower().upper().lower()
token_size = len(converted) * 2

# Dummy state tracking with no impact
state_log = []
for i in range(3):
    if i % 2 == 0:
        state_log.append(f"Stage {i} complete")

interim_result = productivity + risk_factor * 2

# Early termination red herring
if interim_result > 50:
    dummy_offset = 999
else:
    temp_value = interim_result ** 0.5

final_score = evaluate_performance(productivity, risk_factor)

# Helper function defined after use (but still valid in Python scope if called later)
def evaluate_performance(eff, risk):
    base = eff * 2.0
    penalty = risk * 10
    # Use list comprehension and set operation
    adjustments = [i * 2 for i in range(1, 4)]
    adjustment_set = {x for x in adjustments if x > 4}
    total_adjust = sum(adjustment_set)
    result = base + total_adjust - penalty
    return int(result)

print(f"Result: {final_score}")