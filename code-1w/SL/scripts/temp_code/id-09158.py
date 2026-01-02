import itertools

def analyze_sequence(patterns):
    # Irrelevant helper function – never called
    counter = 0
    for p in patterns:
        if len(p) % 2 == 0:
            counter += sum([x ** 0.5 for x in p if x > 0])
    return counter

def preprocess_metrics(raw):
    # Dead code path: this function is defined but unused
    return [x * 1.05 for x in raw if x > 10]

def transform_entry(entry):
    # Unused transformation – red herring
    a, b = entry
    return (a ^ b) + (a & 5)

def filter_outliers(data, limit=100):
    # This function is used, but contains distracting logic
    cleaned = []
    temp_sum = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            temp_sum += val // 2
        if val < limit:
            cleaned.append(val * 1.1)
    adjustment = sum(cleaned) / len(cleaned) if cleaned else 0
    # Only the length matters in the real logic; rest is distraction
    return len(cleaned), adjustment

def build_context(keys, values):
    # Creates a dictionary but only one field is actually used later
    ctx = dict(zip(keys, values))
    ctx['checksum'] = sum(values) - len(keys)
    ctx['version'] = '2.1'
    ctx['active'] = True
    return ctx

def evaluate_performance(metrics, config):
    # Core logic hidden among multiple distractions
    base = 0
    for i, val in enumerate(metrics):
        if i % 2 == 0 and val > config['threshold']:
            base += val * 0.8
        elif val <= config['floor']:
            base += val * 0.3

    # Distractor: complex-looking but unused bitwise operation
    decoy_mask = 0b110101
    masked_base = base ^ decoy_mask | 7

    # Real use of itertools: only this part matters
    rolling = list(itertools.accumulate(metrics[:4], lambda x, y: x + y//3))
    bonus = rolling[-1] if len(rolling) >= 4 else 0

    # Another red herring: tuple unpacking with irrelevant variables
    meta_info = ('debug', 'mode_off', 0xDEADBEEF)
    mode_name, _, flag_code = meta_info

    # Conditional branch with misleading intermediate
    if flag_code in [0xFEEDBEEF, 0xDEADBEEF]:
        bonus -= 5  # This executes, but offset by later logic

    # Key data structure manipulation – sets used to deduplicate fake metrics
    fake_stream = [10, 20, 30, 20, 40]
    seen = set()
    unique_fake = []
    for x in fake_stream:
        if x not in seen:
            unique_fake.append(x)
            seen.add(x)
    # Nothing from unique_fake is used

    # Actual answer contribution: bonus is critical
    final = base + bonus

    # Multiple assignments – only last one matters
    temp_a, temp_b = 100, 200
    temp_a = final - 15

    # Final assignment
    final_score = int(temp_a)

    # Decoy print statements (not executed)
    # print(f'Debug: {masked_base}, {len(unique_fake)}, {mode_name}')

    return final_score

# Main execution flow
if __name__ == '__main__':
    # Input data setup – realistic domain: system performance metrics
    metric_data = [120, 45, 88, 63, 92, 50]
    
    # Threshold configuration – only 'threshold' and 'floor' are used
    thresholds = {
        'threshold': 60,
        'floor': 55,
        'window': 5,
        'debug_mode': False,
        'timeout': 300
    }
    
    # Irrelevant list transformations
    indexed = list(enumerate([x * 2 for x in metric_data]))
    paired = list(zip([1, 0, 1, 0, 1, 0], metric_data))
    
    # Unused dictionary operations
    stats = {'mean': sum(metric_data)/len(metric_data), 'peak': max(metric_data)}
    stats.update({'lag': 4})
    
    # Critical execution point
    final_score = evaluate_performance(metric_data, thresholds)
    
    # Output result
    print(f"Target result: {final_score}")