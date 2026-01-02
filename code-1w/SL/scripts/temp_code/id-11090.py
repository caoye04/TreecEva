from collections import defaultdict

# Simulate a warehouse inventory system with inflow and outflow tracking
def calculate_inventory_flow():
    inbound_shipments = [120, 150, 95, 200, 60]
    outbound_orders = [89, 155, 43, 110, 77]
    returns = [12, 8, 19, 5, 3]
    adjustments = [-5, 10, -3, 7, -12]

    # Track daily net movement
    daily_net = []
    cumulative_buffer = 0
    spike_detected = False
    spike_counter = 0

    # Auxiliary tracking structures (some used, some not)
    flow_history = defaultdict(int)
    anomaly_log = []
    temp_shadow_sum = 0  # Distractor: used for fake validation

    for i in range(len(inbound_shipments)):
        inflow = inbound_shipments[i]
        outflow = outbound_orders[i]
        returned_items = returns[i]
        adj = adjustments[i]

        gross_in = inflow + returned_items
        gross_out = outflow

        net_daily = gross_in - gross_out + adj
        daily_net.append(net_daily)

        # Fake anomaly detection (distractor logic)
        if net_daily > 50 and not spike_detected:
            spike_detected = True
            spike_counter += 1
            anomaly_log.append((i, net_daily))

        # Real accumulation
        cumulative_buffer += abs(net_daily)  # Used in fake metric

        # Shadow sum distraction
        temp_shadow_sum += net_daily * 0.1  # Irrelevant computation

        # Record in history
        flow_history[f'day_{i}'] = net_daily

    # Secondary processing: filter significant flows
    significant_flows = [x for x in daily_net if abs(x) > 20]
    volatility_index = sum([abs(x) for x in significant_flows]) // len(significant_flows)

    # Distractor: unused complex structure
    summary_stats = {
        'peak_inflow': max(inbound_shipments),
        'peak_outflow': max(outbound_orders),
        'total_returns': sum(returns),
        'adjustment_sum': sum(adjustments),
        'buffer_snapshot': cumulative_buffer,
        'volatility': volatility_index
    }

    # Core calculation chain
    base_flow = sum(daily_net)
    modifier = summary_stats['volatility'] // 5
    correction_factor = 1 if base_flow >= 0 else -1
    adjusted_volatility = abs(modifier) * correction_factor

    # Final aggregation
    net_flow = base_flow + adjusted_volatility

    # Last-minute tweak based on pattern
    if len([x for x in daily_net if x < 0]) >= 3:
        adjustment = -8
    else:
        adjustment = 12

    final_balance = net_flow + adjustment

    # Print required result
    print(f"Result: {net_flow}")

    return final_balance

# Execute function
calculate_inventory_flow()