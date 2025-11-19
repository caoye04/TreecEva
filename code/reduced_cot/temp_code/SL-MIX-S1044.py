suspicious_patterns = ['<script>', 'DROP TABLE', '../etc/passwd']
known_threat_hashes = {hash(pattern) for pattern in suspicious_patterns}
current_payload = 'SELECT * FROM users; DROP TABLE users;'
payload_fragments = current_payload.split('; ')
fragment_hashes = [hash(fragment) for fragment in payload_fragments]
matching_hashes = known_threat_hashes.intersection(set(fragment_hashes))
intrusion_score = len(matching_hashes) * 10
print(f'Result: {intrusion_score}')