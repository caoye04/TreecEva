def analyze_trend(values):
    trend = 0
    for i, v in enumerate(values):
        if i > 0:
            diff = v - values[i-1]
            trend += 1 if diff > 0 else (-1 if diff < 0 else 0)
    return trend


def validate_range(vals, low, high):
    # Irrelevant validation function (not used in final logic)
    return all(low <= v <= high for v in vals)


def calculate_volatility(prices):
    mean_price = sum(prices) / len(prices)
    variance = sum((p - mean_price) ** 2 for p in prices) / len(prices)
    return variance ** 0.5


def calculate_final_score(data, thresholds):
    base_score = 0
    adjustments = []
    
    # Extract components
    temperatures = [row[0] for row in data]
    pressures = [row[1] for row in data]
    flows = [row[2] for row in data]
    
    # Misleading intermediate calculations (some irrelevant)
    temp_trend = analyze_trend(temperatures)
    pressure_volatility = calculate_volatility(pressures)
    flow_efficiency = sum(flows) / (max(flows) + 1e-5)
    
    # Dummy stats (unused but look important)
    avg_pressure = sum(pressures) / len(pressures)
    max_flow_index = [i for i, f in enumerate(flows) if f == max(flows)][0] if flows else -1
    
    # Core logic begins
    score_components = list(zip(temperatures, pressures, flows))
    
    for idx, (t, p, f) in enumerate(score_components):
        # Conditional expression with logical and bitwise mix
        base_increment = 10 if t > thresholds['temp'] else 5
        pressure_factor = 1.2 if p & 1 else 0.8  # bitwise AND as red herring
        flow_boost = 1.5 if f > thresholds['flow'] and p > thresholds['pressure'] else 1.0
        
        # Accumulate adjustment
        adjustment = base_increment * pressure_factor * flow_boost
        adjustments.append(adjustment)
        
        # Extra distraction: simulate state tracking
        if idx % 2 == 0:
            dummy_state = (idx | 3) ^ 1  # meaningless bitwise ops
            base_score -= dummy_state * 0.1  # tiny irrelevant deduction
    
    # Final computation
    total_adjustment = sum(a for a in adjustments if a >= 9)  # filter significant ones
    penalty = len([a for a in adjustments if a < 9]) * 2
    base_score += total_adjustment - penalty
    
    # One last conditional twist
    final_multiplier = 1.1 if temp_trend > 0 else 0.9
    
    return int(base_score * final_multiplier)

# Main execution
if __name__ == "__main__":
    # Input data: [temperature, pressure, flow_rate]
    data = [
        [70, 102, 25],
        [74, 105, 23],
        [77, 103, 30],
        [80, 108, 35],
        [85, 107, 33]
    ]
    
    thresholds = {
        'temp': 75,
        'pressure': 104,
        'flow': 28
    }
    
    # Unused variables (distractors)
    calibration_sequence = [x % 7 for x in range(15)]
    system_status = "STABLE" if sum(calibration_sequence) < 50 else "ERROR"
    backup_thresholds = {k: v * 1.1 for k, v in thresholds.items()}
    
    # Key statement
    final_score = calculate_final_score(data, thresholds)
    
    print(f"Result: {final_score}")