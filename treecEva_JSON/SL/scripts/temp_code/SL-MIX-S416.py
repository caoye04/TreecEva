def transform_fingerprint(fp, depth=3):
    if depth == 0:
        return fp
    else:
        transformed = (fp << 1) ^ (fp >> 2) & 0xFF
        return transform_fingerprint(transformed, depth-1)

def generate_session_key(device_data):
    base_key = 0
    for device_id, features in device_data.items():
        fingerprint = sum(features.values()) & 0xFF
        transformed_fp = transform_fingerprint(fingerprint)
        base_key ^= transformed_fp
    return base_key

def validate_key(key):
    match key & 0x0F:
        case 0x01: return key | 0x10
        case 0x02: return key | 0x20
        case 0x03: return key | 0x30
        case _: return key & 0xF0

class KeyManager:
    def __init__(self):
        self.keys = {}
    
    def __enter__(self):
        device_profiles = {
            'dev_001': {'cpu': 8, 'ram': 16, 'storage': 512},
            'dev_002': {'cpu': 4, 'ram': 8, 'storage': 256},
            'dev_003': {'cpu': 16, 'ram': 32, 'storage': 1024}
        }
        self.keys = {dev_id: sum(features.values()) for dev_id, features in device_profiles.items()}
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

with KeyManager() as km:
    enhanced_profiles = {dev_id: {f'feature_{i}': val for i, val in enumerate([cpu*2, ram+4, storage//2])} 
                        for dev_id, total in km.keys.items()
                        for cpu, ram, storage in [(total//28, total//14, total*2)]}
    
    session_key = generate_session_key(enhanced_profiles)
    session_key = validate_key(session_key)

print(f"Result: {session_key}")