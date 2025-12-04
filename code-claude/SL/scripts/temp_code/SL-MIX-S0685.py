def validate_path(path):
    # Check if path has valid structure
    if not path or len(path) < 2:
        return False
    
    # Decoy validation that looks important but isn't used
    checksum = sum([ord(c) for c in path]) % 256
    path_type = 'network' if '//' in path else 'local'
    
    # Actual validation logic
    segments = path.split('/')
    if segments[0] == '':
        segments = segments[1:]
    
    # Misleading condition that's always false for our paths
    if path_type == 'network' and checksum < 128:
        return False
    
    # The real validation check
    return len(segments) >= 2 and not any(s == '..' for s in segments)

def analyze_network_load(paths, threshold=5):
    # Decoy function that calculates something that looks important
    load_factors = [len(p.split('/')) * 2.5 for p in paths]
    avg_load = sum(load_factors) / len(load_factors) if load_factors else 0
    return avg_load > threshold

# Initialize with some sample paths
paths = [
    '/home/user/documents',
    '/var/log/system',
    '/etc/config',
    '../temp/cache',
    '/usr/bin',
    '/home/user/../downloads',
    '/opt',
    '//network/share'
]

# Some misleading preprocessing and filtering
processed_paths = [p.replace('\\', '/') for p in paths]
duplicate_count = len(paths) - len(set(paths))
processed_paths.extend(['/decoy/path1', '/decoy/path2'])

# Track some metrics that look relevant but aren't used for the answer
path_metrics = {}
for p in processed_paths:
    depth = p.count('/')
    path_metrics[p] = {
        'depth': depth,
        'segments': len(p.split('/')),
        'is_absolute': p.startswith('/')
    }

# More misleading calculations
total_depth = sum(m['depth'] for m in path_metrics.values())
avg_depth = total_depth / len(path_metrics) if path_metrics else 0

# Apply some filters to the paths
filter_condition = lambda p: p.startswith('/') and len(p) > 5
filtered_paths = [p for p in paths if filter_condition(p)]

# This is where the answer is calculated
valid_paths = len([p for p in filtered_paths if validate_path(p)])

# More distraction after the answer
system_health = 100 - (duplicate_count * 5) - (0 if analyze_network_load(filtered_paths) else 10)
if system_health < 80:
    valid_paths_backup = valid_paths  # This never executes
    valid_paths = -1                 # This never executes

# Additional calculations that look important but don't affect the answer
efficiency_score = (valid_paths / len(paths)) * 100 if paths else 0
network_impact = sum(1 for p in filtered_paths if '//' in p) * 2.5

print(f"Result: {valid_paths}")
