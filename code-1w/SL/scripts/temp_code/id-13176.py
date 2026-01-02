from itertools import combinations

# Simulate a system that evaluates algorithmic trading strategy performance
# with multiple filtering and scoring stages

def evaluate_performance(weights, outcomes):
    # weights: importance of volatility, return, drawdown, consistency
    # outcomes: actual measured values from backtest

    volatility_score = outcomes[0] * weights[0]
    return_score = outcomes[1] * weights[1]
    drawdown_penalty = outcomes[2] * weights[2]
    consistency_bonus = outcomes[3] * weights[3]

    # Intermediate irrelevant computation (distractor)
    max_combinations = list(combinations([1, 2, 3, 4, 5], 3))
    combination_count = len(max_combinations)  # Not used in final score

    baseline_adjustment = 0.85
    adjusted_return = return_score * baseline_adjustment

    # Dummy loop for complexity (does not affect result)
    temp_accum = 0
    for i in range(3):
        for j in range(2):
            temp_accum += i * j * 0.1  # Irrelevant accumulation

    # Real scoring logic
    raw_score = volatility_score + adjusted_return - drawdown_penalty + consistency_bonus

    # Apply non-linear boost (real impact)
    if raw_score > 6:
        boosted_score = raw_score * 1.15
    else:
        boosted_score = raw_score

    # Normalize to scale (key transformation)
    normalized_score = round(boosted_score * 10, 2)

    # Additional red herring: simulate risk tiers
    risk_tier = ""
    if normalized_score > 85:
        risk_tier = "High"
    elif normalized_score > 60:
        risk_tier = "Medium"
    else:
        risk_tier = "Low"

    # Final assignment — this is the target variable
    final_score = int(normalized_score)

    return final_score

# Input data
metric_weights = [0.2, 0.5, 0.3, 0.15]  # Volatility, Return, Drawdown, Consistency
raw_outcomes = [4.0, 12.0, 2.5, 3.8]   # Measured metric values

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Result: {final_score}")