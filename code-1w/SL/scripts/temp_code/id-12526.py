from collections import Counter

# System log analysis: tracking unique error signatures across modules
defect_logs_a = ['E101', 'E102', 'E103', 'E104', 'E101', 'E105']
defect_logs_b = ['E103', 'E104', 'E105', 'E106', 'E107', 'E103']

# Extract unique errors from each module (maintaining signature diversity)
unique_a = set(defect_logs_a)
unique_b = set(defect_logs_b)

# Find shared error signatures between modules
shared_errors = unique_a.intersection(unique_b)

# Simulate post-processing filter: errors that passed diagnostic validation
validation_registry = ['E104', 'E105', 'E106', 'E108']
processed_items = set(validation_registry)

# Track which shared errors were successfully processed
final_overlap = unique_a & unique_b & processed_items

# Auxiliary metric: frequency distribution of all defects (distractor)
all_defects = defect_logs_a + defect_logs_b
defect_freq = Counter(all_defects)

# Secondary derived value: number of unique unprocessed shared errors (distractor)
unprocessed_count = len(shared_errors - processed_items)

Result: final_overlap