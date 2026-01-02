def assess_system_risk(nodes, thresholds):
    risk_levels = []
    for i, (node_val, thresh) in enumerate(zip(nodes, thresholds)):
        if node_val > thresh:
            risk_levels.append(i * (node_val & (thresh + 1)))
        elif node_val == thresh:
            risk_levels.append(-i)
    masked_levels = [level for level in risk_levels if level > -5]
    filtered_risk_indices = [level for level in masked_levels if level % 2 == 1]
    result = sum(filtered_risk_indices)
    return result

# Simulated sensor node readings and safety thresholds
telemetry_nodes = [12, 15, 10, 24, 8]
safety_thresholds = [10, 15, 8, 16, 9]

final_output = assess_system_risk(telemetry_nodes, safety_thresholds)
print(f"Result: {final_output}")