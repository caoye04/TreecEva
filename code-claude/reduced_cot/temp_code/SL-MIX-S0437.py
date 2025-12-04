# Customer Support Ticket Priority Calculator

# Ticket information
ticket_id = "TKT-4289"
ticket_type = "technical"
is_urgent = True
waiting_time = 45  # minutes

# Calculate base score from waiting time
base_score = waiting_time // 10
if waiting_time % 10 >= 5:
    base_score += 1

# Additional factors
urgency_factor = 0.5
penalty = 2

# Set customer tier based on subscription
subscription = "premium"
customer_tier = 2 if subscription == "premium" else 1

# Apply customer tier adjustment
base_score = base_score + customer_tier

# Calculate final priority score
priority_score = base_score * (1 + urgency_factor) if is_urgent else base_score - penalty

# Additional optional adjustments (not applied in this case)
weekend_bonus = 3
holiday_bonus = 5

print(f"Result: {priority_score}")