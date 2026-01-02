def analyze_trends(values, baseline):
    trend_data = {}
    up_count = 0
    down_count = 0
    neutral_count = 0
    volatility_index = 0.0

    for i, val in enumerate(values):
        if val > baseline * 1.1:
            trend_data[i] = 'up'
            up_count += 1
        elif val < baseline * 0.9:
            trend_data[i] = 'down'
            down_count += 1
        else:
            trend_data[i] = 'neutral'
            neutral_count += 1

        if i > 0:
            change = abs(val - values[i-1])
            volatility_index += change

    # Distractor: unused transformation
    transformed = [x ** 0.5 for x in values if x > 0]
    avg_transform = sum(transformed) / len(transformed) if transformed else 0

    return up_count, down_count, neutral_count, volatility_index


def compute_final_score(data, thresholds):
    raw_scores = []n    adjustment_factor = 0.0
    total_weight = 0.0

    for key, values in data.items():
        base_ref = sum(values) / len(values)
        
        # Simulate threshold-based scoring
        if base_ref > thresholds['high']:
            score = 90 + (base_ref - thresholds['high']) * 2
        elif base_ref < thresholds['low']:
            score = 30 - (thresholds['low'] - base_ref) / 2
        else:
            score = 60 + (base_ref - thresholds['mid'])

        # Additional logic with distractors
        if len(values) > 5:
            max_val = max(values)
            min_val = min(values)
            range_ratio = (max_val - min_val) / base_ref if base_ref else 0
            
            # Distractor: this modifies score but is later overwritten
            if range_ratio > 0.5:
                adjustment_factor += 5
            else:
                adjustment_factor -= 2

        # Real score adjustment based on trends
        up_trend, down_trend, _, vol_idx = analyze_trends(values, base_ref)
        if up_trend > down_trend:
            score += 10
        elif down_trend > up_trend:
            score -= 10

        # Volatility penalty
        normalized_vol = vol_idx / len(values)
        if normalized_vol > 15:
            score -= 8

        raw_scores.append(score)

        # Dead code path — never executed due to logic above
        if False and key == "phantom":
            fallback = sum([x*x for x in values])
            raw_scores.append(fallback)

    # Final aggregation
    final_raw = sum(raw_scores) / len(raw_scores) if raw_scores else 0
    
    # Irrelevant smoothing
    smoothed = [final_raw * 0.95, final_raw * 1.05]
    temp_avg = sum(smoothed) / len(smoothed)

    # Actual final computation
    threshold_bonus = 5 if temp_avg > 70 else -5
    final_score = int(final_raw + threshold_bonus + adjustment_factor)

    return final_score

# Main execution
if __name__ == '__main__':
    dataset = {
        'Q1_sales': [120, 135, 130, 145, 160, 170],
        'Q2_sales': [150, 148, 155, 140, 138, 142, 146],
        'expenses': [80, 85, 90, 95, 100, 105],
        'support_tickets': [20, 25, 18, 22, 24, 21]
    }
    
    limits = {
        'low': 90,
        'mid': 110,
        'high': 130
    }
    
    # Intermediate unused analysis
    all_vals = [val for sublist in dataset.values() for val in sublist]
    global_mean = sum(all_vals) / len(all_vals)
    outlier_count = len([v for v in all_vals if abs(v - global_mean) > 2 * (sum((x - global_mean)**2 for x in all_vals)/len(all_vals))**0.5])
    
    final_score = compute_final_score(dataset, limits)
    print(f"Result: {final_score}")