# Candidate selection system for a tech company
# The system evaluates applicants based on scores in different assessment areas

def calculate_bonus_points(years_exp):
    if years_exp > 5:
        return 15
    elif years_exp > 2:
        return 8
    return 0

# Initialize applicant data
applicant_scores = {
    'A101': 78,
    'B202': 92,
    'C303': 65,
    'D404': 88,
    'E505': 72,
    'F606': 84
}

# Experience data (not directly used in final selection)
experience_years = {
    'A101': 1,
    'B202': 6,
    'C303': 3,
    'D404': 2,
    'E505': 4,
    'F606': 7
}

# Calculate potential adjustments (not applied in this phase)
potential_adjustments = {}
for applicant_id, years in experience_years.items():
    bonus = calculate_bonus_points(years)
    potential_adjustments[applicant_id] = bonus
    
# Track rejected candidates for future reference
rejected_candidates = []

# Set selection parameters
max_positions = 4
base_threshold = 75
adjustment_factor = 0

# Company decided not to use the adjustment factor this time
if adjustment_factor > 0:
    for applicant_id in applicant_scores:
        applicant_scores[applicant_id] += potential_adjustments.get(applicant_id, 0)

# Calculate the actual threshold
threshold = base_threshold + adjustment_factor

# Identify candidates who meet the threshold
qualified_candidates = len([id for id in applicant_scores if applicant_scores[id] >= threshold])

# Track rejected candidates
for applicant_id in applicant_scores:
    if applicant_scores[applicant_id] < threshold:
        rejected_candidates.append(applicant_id)

# Verify we don't exceed maximum positions
if qualified_candidates > max_positions:
    overflow = qualified_candidates - max_positions
    print(f"Warning: {overflow} qualified candidates exceed available positions")

print(f"Result: {qualified_candidates}")