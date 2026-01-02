def analyze_sentiment(text):
    # Irrelevant helper function – distractor
    return sum(1 for c in text if c.lower() in 'aeiou')


def preprocess_data(raw):
    # Distractor: complex-looking but unused data transformation
    cleaned = [x.strip().upper() for x in raw.split(',')]
    return sorted(cleaned, key=len)

# Unused global variables – red herring
baseline = [3, 1, 4, 1, 5]
dummy_mask = [0, 1, 0, 1, 1]
offset_correction = 7

# Key data structure with meaningful and irrelevant entries
evaluation_matrix = {
    'threshold': 65,
    'penalties': {'minor': 2, 'major': 8},
    'weights': [0.1, 0.3, 0.6],
    'debug_mode': True,
    'history': []
}

# Input sequence that will be processed
feedback_sequence = 'A,B,C,A,B,B,C,A'

# Dead code path – never executed, but looks important
def legacy_calculate(seq):
    total = 0
    for item in seq:
        total += ord(item) % 5
    return total // 3

# Simulated sensor drift correction – irrelevant distraction
current_drift = 0.003
for i in range(5):
    current_drift *= 0.9

# Real logic begins here: counting feedback occurrences
def count_feedback_responses(seq):
    labels = seq.split(',')
    counts = {}
    for label in labels:
        clean_label = label.strip()
        counts[clean_label] = counts.get(clean_label, 0) + 1
    return counts  # Returns {'A': 3, 'B': 3, 'C': 2}

# Apply weight-based scoring using dictionary lookup and slicing
def apply_weighted_scoring(counts):
    # Assign points per feedback type
    points_map = {'A': 10, 'B': 7, 'C': 4}
    scores = []
    
    for key in sorted(counts.keys()):
        raw_score = counts[key] * points_map[key]
        scores.append(raw_score)
    
    # Use slicing to ignore lowest score (simulate trimming outlier)
    sorted_scores = sorted(scores)
    trimmed = sorted_scores[1:]  # Remove lowest score
    
    # Weighted combination using evaluation_matrix weights (only some used)
    combined = 0
    for i, val in enumerate(trimmed):
        combined += val * evaluation_matrix['weights'][i % 3]
    
    return round(combined, 6)

# Additional distraction: bit manipulation with no effect on result
status_flag = 0b1010101
status_flag ^= 0b1111
status_flag |= (status_flag << 2)
status_flag &= ~0b1010  # Final flag value unused

# Decoy list processing with sorting and search (dead end)
recent_logs = ['entry_3', 'entry_1', 'entry_4', 'entry_2']
sorted_logs = sorted(recent_logs)
position = -1
for idx, log in enumerate(sorted_logs):
    if 'entry_3' in log:
        position = idx

# Main evaluation function that combines control flow, dict ops, and slicing
def evaluate_performance(seq):
    count_result = count_feedback_responses(seq)
    
    # Extract values and sort them for slicing operation
    values = sorted(list(count_result.values()))
    mid_values = values[1:-1]  # Take middle values only
    
    # Compute base performance
    base = sum(mid_values) * 5
    
    # Conditional penalty logic (short-circuit evaluation)
    has_major_issue = count_result.get('C', 0) > 2 and len(seq) > 10
    penalty = evaluation_matrix['penalties']['major'] if has_major_issue else evaluation_matrix['penalties']['minor']
    
    # Apply adjustment
    adjusted = base - penalty
    
    # Final non-linear transformation
    final = int((adjusted ** 1.5) / 10) + offset_correction  # offset_correction is a red herring!
    
    # The real answer is computed here
    return final

# Execution flow starts here
raw_input = "X,Y,Z"  # Unused input – misleading
preprocess_data(raw_input)  # Called but result ignored

# Actual computation chain
interim_scores = apply_weighted_scoring(count_feedback_responses(feedback_sequence))

# Critical execution point
final_score = evaluate_performance(feedback_sequence)

# Output result as required
print(f"Target result: {final_score}")