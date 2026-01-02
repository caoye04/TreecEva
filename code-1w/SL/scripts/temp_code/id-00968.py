from itertools import compress, count

# Simulated sensor readings over time (temperature, pressure, flow_rate)
sensor_data = [
    (23.5, 98.2, 1.02),
    (24.1, 99.0, 0.98),
    (25.3, 101.5, 1.05),
    (26.0, 103.1, 0.94),
    (24.8, 100.3, 1.01),
    (27.2, 105.6, 0.89),
    (26.8, 104.2, 0.93),
    (25.9, 102.8, 0.97)
]

# Thresholds for normal operation
TEMP_LIMIT = 26.5
PRESSURE_LIMIT = 104.0
FLOW_LOWER_BOUND = 0.95

# Derived metrics
temperatures = [entry[0] for entry in sensor_data]
pressures = [entry[1] for entry in sensor_data]
flow_rates = [entry[2] for entry in sensor_data]

# Calculate moving average of temperature using lambda and zip
moving_avg_temp = list(map(lambda pair: (pair[0] + pair[1]) / 2, 
                            zip(temperatures, temperatures[1:])))

# Identify high-risk intervals where temp > limit OR pressure > limit
high_risk_mask = [t > TEMP_LIMIT or p > PRESSURE_LIMIT 
                   for t, p in zip(temperatures, pressures)]

# Count consecutive high-risk states
consecutive_counter = 0
max_consecutive_risk = 0
for is_risky in high_risk_mask:
    if is_risky:
        consecutive_counter += 1
        max_consecutive_risk = max(max_consecutive_risk, consecutive_counter)
    else:
        consecutive_counter = 0

# Compute baseline health score based on averages
avg_temp = sum(temperatures) / len(temperatures)
avg_pressure = sum(pressures) / len(pressures)
avg_flow = sum(flow_rates) / len(flow_rates)

baseline_health_score = 100 - (
    abs(avg_temp - 25.0) * 2 + 
    abs(avg_pressure - 100.0) * 1.5 + 
    abs(1.0 - avg_flow) * 5
)

# Anomaly detection: count how many readings violate multiple thresholds
multi_violations = 0
for t, p, f in sensor_data:
    violations = 0
    if t > TEMP_LIMIT: violations += 1
    if p > PRESSURE_LIMIT: violations += 1
    if f < FLOW_LOWER_BOUND: violations += 1
    if violations >= 2:
        multi_violations += 1

# Secondary metric: ignored in final calculation but adds distraction
distress_index = multi_violations * 10 + max_consecutive_risk

# Penalty logic
base_penalty = multi_violations * 8
length_penalty = max_consecutive_risk * 3
anomaly_penalty = base_penalty + length_penalty * (1.5 if max_consecutive_risk > 2 else 1.0)

# Use itertools.compress to get only stable flow readings
stable_flow_mask = [f >= FLOW_LOWER_BOUND for f in flow_rates]
stable_flows = list(compress(flow_rates, stable_flow_mask))

# Extraneous statistical measure (unused)
flow_variance = sum((x - avg_flow)**2 for x in flow_rates) / len(flow_rates) if flow_rates else 0

# Final aggregation with key statement
aggregate_health_score = baseline_health_score - (max_consecutive_risk * 2)
final_diagnostic = aggregate_health_score + anomaly_penalty

print(f"Result: {final_diagnostic}")