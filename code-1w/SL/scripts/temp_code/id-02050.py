def calculate_performance(base, adjustments):
    temp = base * 1.1
    if temp < 50:
        temp += adjustments[0]
    else:
        temp += sum(adjustments)
    return round(temp, 2)

# Irrelevant utility function (minor distraction)
def format_message(text):
    return text.upper().replace(' ', '_')

# Setup data
baseline = 45
adjustments = [8, -3, 5]
flag_active = True

# Key computation
final_score = calculate_performance(baseline, adjustments)

# Output result
print(f"Result: {final_score}")