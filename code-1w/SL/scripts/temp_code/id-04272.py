def analyze_pattern(sequence):
    # Irrelevant helper function – dead code path
    return sum(1 for c in sequence if c in 'aeiou')


def preprocess_data(raw):
    # Distractor: string manipulation with no impact on final result
    cleaned = ''.join(filter(str.isalpha, raw.lower()))
    reversed_clean = cleaned[::-1]
    return len(reversed_clean)

# Unused global variables – red herring
user_context = {'mode': 'debug', 'version': 3.7, 'active': False}
config_flags = [True, False, True, True]

# Key data structures
metrics_log = [
    {'epoch': 1, 'loss': 0.52, 'acc': 0.91, 'batch': 32},
    {'epoch': 2, 'loss': 0.48, 'acc': 0.93, 'batch': 64},
    {'epoch': 3, 'loss': 0.45, 'acc': 0.94, 'batch': 32},
    {'epoch': 4, 'loss': 0.40, 'acc': 0.95, 'batch': 128},
    {'epoch': 5, 'loss': 0.38, 'acc': 0.96, 'batch': 64}
]

threshold_set = {0.42, 0.89, 0.92, 0.95}  # Set used in filtering

# Decoy dictionary – looks important but unused
summary_stats = {
    'mean_loss': 0.0,
    'max_acc': 0.0,
    'convergence_epoch': None,
    'flagged_anomalies': []
}

# Auxiliary list – irrelevant character counts
char_analysis = [preprocess_data(f"log_{i}") for i in range(len(metrics_log))]

# Bitwise decoy operation
obfuscation_key = (17 ^ 23) & 0xFF
mask_applied = obfuscation_key << 2

# Simulated conditionals with misleading intermediate results
trigger_event = False
if len(char_analysis) > 3:
    trigger_event = (mask_applied % 5 == 1)

# Conditional expression red herring
status_flag = 'critical' if trigger_event else 'normal'

# Dictionary operation that seems relevant but isn't part of main logic
for entry in metrics_log:
    entry['status'] = status_flag

# Real logic starts here — deeply nested and obscured
high_acc_epochs = []
for record in metrics_log:
    if record['acc'] > 0.92:
        high_acc_epochs.append(record['epoch'])

# Set intersection to find valid thresholds met
achieved_accuracies = {record['acc'] for record in metrics_log}
valid_thresholds_met = achieved_accuracies & threshold_set

# Complex conditional expression combining boolean and comparison logic
penalty_factor = 2 if len(valid_thresholds_met) >= 3 else (1 if len(high_acc_epochs) > 1 else 0)

# Multi-step calculation buried in distractions
base_score = sum(int(epoch * acc * 10) for epoch, acc in zip(high_acc_epochs, [r['acc'] for r in metrics_log if r['epoch'] in high_acc_epochs]))

# Logical operations with short-circuiting – looks complex but necessary
adjustment = (len(high_acc_epochs) > 0) and (min(high_acc_epochs) <= 3)
adjustment_bonus = adjustment * 15

# Final score computation — the real answer
final_score = base_score - (penalty_factor * 8) + adjustment_bonus

# Additional distraction: unused tuple unpacking
backup_metrics = [(d['epoch'], d['loss']) for d in metrics_log]
epochs, losses = zip(*backup_metrics)

# Another decoy: set difference with no use
unused_diff = threshold_set - {0.95, 0.96}

# Print required output
Result: {final_score}