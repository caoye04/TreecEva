def analyze_performance(metrics, thresholds):
    alert_count = 0
    stable_count = 0
    for i, (metric, threshold) in enumerate(zip(metrics, thresholds)):
        if metric > threshold * 1.2:
            alert_count += 1
        elif metric < threshold * 0.8:
            stable_count += 1
    return alert_count


def adjust_metrics(raw_data):
    adjusted = []
    offset = len(raw_data) // 4
    temp_sum = 0
    for idx, val in enumerate(raw_data):
        if idx % 2 == 0:
            adjusted.append(val * 1.1 + offset)
        else:
            adjusted.append(val * 0.9 - offset)
        temp_sum += val
    # Irrelevant smoothing pass
    smoothed = [adjusted[0]]
    for i in range(1, len(adjusted)):
        smoothed.append((smoothed[-1] + adjusted[i]) / 2)
    return adjusted


def rank_entries(data_list):
    sorted_data = sorted(data_list, reverse=True)
    ranks = {}
    for index, value in enumerate(sorted_data):
        ranks[value] = index + 1
    rank_sum = sum(ranks.values())
    avg_rank = rank_sum / len(ranks)
    # Dummy tracking
    above_avg = [v for v in data_list if v > avg_rank]
    return ranks


def apply_correction(ranks, factor=0.5):
    corrected = {}
    total_corr = 0
    for key, rank in ranks.items():
        corrected[key] = key - factor * rank
        total_corr += factor * rank
    norm_factor = max(corrected.values()) if corrected else 1
    normalized = {k: v / norm_factor for k, v in corrected.items()}
    return list(normalized.values())


def calculate_final_score(rankings, adjustments):
    base_score = 0
    penalty = 0
    for i, rank in enumerate(rankings):
        if i % 3 == 0:
            base_score += rank * 2
        elif i % 3 == 1:
            base_score += rank
        else:
            penalty += 1
    adjustment_sum = sum(abs(a) for a in adjustments)
    final_score = base_score - penalty * 3 + (adjustment_sum // 10)
    
    # Redundant validation block (dead-end logic)
    validation_check = 0
    for j in range(len(adjustments)):
        if j < len(rankings) and rankings[j] > 2:
            validation_check += adjustments[j] // 2
    # Unused intermediate values
    outlier_detect = [x for x in adjustments if x > 15]
    shift_offset = len(outlier_detect) * 2
    
    return final_score

# Main execution flow
metrics = [85, 90, 78, 92, 88]
thresholds = [80, 87, 75, 85, 90]
raw_data = [100, 200, 150, 180, 120]

# Step 1: Analyze performance (distractor call)
analyze_performance(metrics, thresholds)

# Step 2: Adjust raw metrics
adjusted_metrics = adjust_metrics(raw_data)

# Step 3: Rank the original raw data
rank_dict = rank_entries(raw_data)
rankings = list(rank_dict.values())

# Step 4: Apply correction to ranks (semi-relevant)
corrected_values = apply_correction(rank_dict, factor=0.5)

# Step 5: Calculate final score using rankings and adjustments
final_score = calculate_final_score(rankings, adjusted_metrics)

print(f"Result: {final_score}")