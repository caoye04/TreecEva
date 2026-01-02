from itertools import compress, cycle
import math

def calculate_headroom(value, limit=100):
    # Irrelevant helper function for distraction
    return limit - value if value < limit else 0

def adjust_pressure(base, rates):
    # Core logic with mixed operations
    scaling_factor = 0.85
    filtered_rates = [r for r in rates if r > 0]
    
    # Distractor: complex but unused computation
    temp_analysis = list(map(lambda x: round(math.log(x + 1) ** 1.5, 3), filtered_rates))
    spike_count = sum(1 for x in filtered_rates if x > 50)
    
    # Relevant state tracking
    cumulative_effect = 0
    for i, rate in enumerate(filtered_rates):
        if i % 2 == 0:
            cumulative_effect += math.sin(rate / 10) * scaling_factor
        else:
            cumulative_effect -= math.cos(rate / 15) * 0.5
    
    # Additional distraction: string-based flagging
    status_flags = ['HIGH' if r > 75 else 'NORMAL' for r in filtered_rates]
    alert_mode = len([f for f in status_flags if f == 'HIGH']) > 2
    
    # Real adjustment based on controlled factors
    volatility_index = abs(cumulative_effect) * 0.1
    base_adjustment = base * (1 + volatility_index)
    
    # Final interference: dead conditional branch
    if alert_mode and False:  # Never executes
        base_adjustment *= 1.2
        extra_log = calculate_headroom(int(base_adjustment))

    # Key assignment
    final_pressure = round(base_adjustment - 10, 4)
    return final_pressure

# Simulation data
flow_data = [23, 45, 52, 12, 88, 67, 34, 9, 71]
base_pressure = 101.325

# Unused transformations for distraction
doubled_flow = [x * 2 for x in flow_data]
decimated_flow = [x for x in doubled_flow if x % 10 == 0]
mask = [i % 3 == 0 for i in range(len(flow_data))]
masked_sample = list(compress(flow_data, mask))

cycle_stream = cycle([10, 20])
cycled_values = [next(cycle_stream) for _ in range(5)]

# Critical execution point
final_pressure = adjust_pressure(base_pressure, flow_rates=flow_data)
print(f"Result: {final_pressure}")