def analyze_trends(data, threshold=0.5):
    moving_avg = sum(data[-3:]) / 3 if len(data) >= 3 else 0
    volatility = max(data) - min(data) if data else 0
    trend = 'up' if data and data[-1] > data[0] else 'down'
    return moving_avg, volatility, trend


def compute_risk_profile(age, assets):
    risk_factor = 100 - age
    adjusted_assets = assets * (risk_factor / 100)
    risk_level = 'high' if adjusted_assets < 50000 else 'moderate' if adjusted_assets < 200000 else 'low'
    return risk_factor, adjusted_assets, risk_level


def generate_insights(revenue, expenses):
    profit = revenue - expenses
    profit_margin = (profit / revenue) * 100 if revenue else 0
    efficiency_ratio = (expenses / revenue) * 100 if revenue else 0
    return profit, profit_margin, efficiency_ratio


def filter_outliers(values, factor=1.5):
    if not values:
        return []
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    filtered = [v for v in values if lower_bound <= v <= upper_bound]
    return filtered


def calculate_composite_weight(a, b, c, weights=(0.3, 0.4, 0.3)):
    weighted_sum = a * weights[0] + b * weights[1] + c * weights[2]
    normalized = weighted_sum / sum(weights)
    return normalized

# Irrelevant utility functions (distractors)
def unused_helper_1(x): return x ** 2 + 1
def unused_helper_2(lst): return [i * 3 for i in lst if i % 2 == 0]

def placeholder_operation():
    temp_data = [1, 2, 3, 4, 5]
    processed = [x * 2 for x in temp_data]
    return sum(processed)

# Misleading variables (red herrings)
misleading_total = 98765
intermediate_flag = True
dummy_counter = 0
useless_list = ['ignore', 'this', 'data']

# Simulated input data
market_data = [0.4, 0.6, 0.55, 0.48, 0.72, 0.61]
user_age = 35
user_assets = 180000
quarterly_revenue = 450000
quarterly_expenses = 360000
raw_metrics = [0.82, 0.75, 0.91, 0.64, 0.88]

# Processing steps with distractions
avg, vol, direction = analyze_trends(market_data)
risk_factor, adj_assets, risk_cat = compute_risk_profile(user_age, user_assets)
profit_val, margin, efficiency = generate_insights(quarterly_revenue, quarterly_expenses)

# Filtering real metric but embedded in noise
filtered_metrics = filter_outliers(raw_metrics, 1.8)
primary_metric = filtered_metrics[-1] if filtered_metrics else 0.5
auxiliary_metric = margin / 100
contextual_metric = vol * 10

# Dummy operations to increase interference
for _ in range(2):
    dummy_counter += 1
    placeholder_operation()  # Dead-end call

if intermediate_flag:
    temp_result = (primary_metric + auxiliary_metric) * 0.5
    secondary_value = temp_result ** 2
else:
    secondary_value = 0.1

# Real computation path buried in logic
metric_a = primary_metric
metric_b = auxiliary_metric
metric_c = contextual_metric * 0.01

composite = calculate_composite_weight(metric_a, metric_b, metric_c)
score_modifier = 1.2 if direction == 'up' and risk_cat != 'high' else 0.8

adjusted_score = composite * score_modifier

# Final transformation using conditional expression and list comprehension distractor
bonus_pool = [x * 0.05 for x in [profit_val, adj_assets, vol] if x > 100]
final_bonus = bonus_pool[0] if len(bonus_pool) > 0 else 0

final_score = adjusted_score * 1000 + final_bonus

# Critical output
Target result: {final_score}