def analyze_temperature(t):
    return t > 37.5

def validate_pressure(p):
    return 100 <= p <= 200

def adjust_flow_rate(flow, temp, pressure):
    factor = 1.0
    if temp < 20:
        factor = 0.8
    elif temp > 40:
        factor = 1.3
    adjusted = flow * factor
    
    # Irrelevant adjustment based on pressure (not used in final logic)
    pressure_flag = validate_pressure(pressure)
    temp_alert = analyze_temperature(temp)
    
    # Distractor computation
    safety_margin = 1.0 if not temp_alert and pressure_flag else 0.9
    
    return adjusted

def generate_state_snapshot(time_idx, base_flow):
    temp = (time_idx * 3.1) % 50
    pressure = (time_idx * 17) % 120 + 140
    flow = (base_flow + time_idx) % 100 + 25
    
    # Dummy transformation
    normalized_temp = round(temp + 0.5)
    scaled_pressure = pressure / 10.0
    
    return {
        't': temp,
        'p': pressure,
        'f': flow,
        'norm_t': normalized_temp,
        'scale_p': scaled_pressure,
        'index': time_idx
    }

def process_state(log):
    cumulative_score = 0
    adjustment_history = []    
    temp_extremes = 0
    total_flow = 0
    
    for entry in log:
        t = entry['t']
        p = entry['p']
        f = entry['f']
        
        # Relevant conditional expression
        flow_mod = adjust_flow_rate(f, t, p)
        
        # Core logic step 1: track total flow
        total_flow += flow_mod
        
        # Core logic step 2: detect high temperature events
        if t > 45:
            temp_extremes += 1
        
        # Core logic step 3: score assignment using conditional expression
        entry_score = 10 if t < 30 else (5 if t < 40 else -2)
        cumulative_score += entry_score
        
        # Irrelevant tracking
        adjustment_history.append(flow_mod * 0.1)
        
        # Dead code path (never accessed in this input range)
        if t < 0:
            cumulative_score -= 100  # unreachable
    
    # Core logic step 4: combine metrics
    avg_flow = total_flow / len(log)
    
    # Core logic step 5: conditional expression affecting output
    stability_bonus = 50 if temp_extremes == 0 and avg_flow > 60 else 20
    
    # Core logic step 6: final computation
    result = int(cumulative_score + stability_bonus)
    
    # Core logic step 7: final adjustment
    final_value = result if result > 0 else 0
    
    # Distractor: unused derived metric
    efficiency_ratio = avg_flow / (cumulative_score + 1) if cumulative_score >= 0 else 0
    
    return final_value

# Main execution
state_log = []
for i in range(8):
    base = (i * 13) % 40
    snapshot = generate_state_snapshot(i, base)
    state_log.append(snapshot)

# Key statement
final_output = process_state(state_log)
print(f"Result: {final_output}")