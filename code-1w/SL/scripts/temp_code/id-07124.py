def adjust_score(value, deduction):
    if value <= 0:
        return 0
    adjusted = value - deduction
    if adjusted < 0:
        adjusted = 0
    return adjusted

# Input processing
raw_input = "85.6"
base_score = float(raw_input.strip())

# Penalty calculation based on format check
input_str = "85.6"
decimals_present = '.' in input_str
penalty = 5 if len(input_str) > 5 or not decimals_present else 2

# Apply adjustment
cleaned_value = base_score  # Simulate preprocessing step
final_score = adjust_score(cleaned_value, penalty)

print(f"Result: {final_score}")