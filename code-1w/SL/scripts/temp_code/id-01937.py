def calculate_performance(base, tweaks):
    adjusted_base = base * 1.1
    penalty = 0
    if len(tweaks) > 3:
        penalty += 5
    for val in tweaks:
        if str(val).isdigit() and int(val) > 10:
            penalty += 2
    aggregate = sum(tweaks) / len(tweaks)
    return int(adjusted_base + aggregate - penalty)

baseline = 65
adjustments = [8, 12, 15, 7]

# Irrelevant utility function (minimal interference)
def format_timestamp(ts):
    return ts.replace('T', ' ').upper()

timestamp = "2023-10-05T14:30:00"
formatted_time = format_timestamp(timestamp)

final_score = calculate_performance(baseline, adjustments)
print(f"Result: {final_score}")