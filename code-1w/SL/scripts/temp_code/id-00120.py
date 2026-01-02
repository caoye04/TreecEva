import hashlib
logs = ['login_success', 'login_failure', 'access_granted', 'login_success', 'access_denied', 'login_failure']
hashes = [hashlib.md5(log.encode()).hexdigest() for log in logs]
unique_hashes = len(set(hashes))
print(f'Result: {unique_hashes}')