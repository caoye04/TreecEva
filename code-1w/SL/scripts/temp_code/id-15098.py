from collections import defaultdict

# System performance monitoring variables
baseline = 150
peak_capacity = 1000
active_users = 204
uptime_hours = 98.6

efficiency_target = 75.0
engagement_score = (active_users * 0.37) + 5

# Irrelevant metric (distractor)
cost_per_user = 1.25
total_cost = active_users * cost_per_user

# Core logic with boolean and arithmetic reasoning
current_load = active_users / peak_capacity
load_percentage = round(current_load * 100, 2)

# Key decision flag based on combined thresholds
threshold_flag = (active_users > baseline) and (engagement_score >= efficiency_target)

# Additional unrelated statistic (minor distraction)
default_error_log = defaultdict(int)
default_error_log['timeout'] += 1

Result: threshold_flag