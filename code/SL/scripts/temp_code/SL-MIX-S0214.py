import re
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Set

def hash_string(s: str) -> int:
    return hash(s) % 1000000

@contextmanager
def hash_tracker():
    matched_hashes: Set[int] = set()
    try:
        yield matched_hashes
    finally:
        pass

@dataclass
class PasswordEntry:
    username: str
    password_hash: int
    is_compromised: bool = False

# Password database
password_entries = [
    PasswordEntry("admin", hash_string("password123")),
    PasswordEntry("user1", hash_string("qwerty")),
    PasswordEntry("guest", hash_string("guest123")),
    PasswordEntry("dev", hash_string("devpass!")),
]

# Common weak password patterns
weak_patterns = [r"password", r"qwerty", r"123", r"admin", r"guest"]

# Known compromised hashes
compromised_hashes = {hash_string("password123"), hash_string("qwerty"), hash_string("123456")}

vulnerability_score = 0

with hash_tracker() as tracked:
    for entry in password_entries:
        # Check if hash is in compromised set
        if entry.password_hash in compromised_hashes:
            entry.is_compromised = True
            vulnerability_score += 10
            tracked.add(entry.password_hash)
        
        # Check for pattern matches
        pattern_match = False
        for pattern in weak_patterns:
            if re.search(pattern, entry.username, re.IGNORECASE):
                pattern_match = True
                break
        
        # Apply scoring logic
        if entry.is_compromised and not pattern_match:
            vulnerability_score += 5
        elif not entry.is_compromised and pattern_match:
            vulnerability_score += 3
        elif entry.is_compromised and pattern_match:
            vulnerability_score += 7
        
        # Additional check for admin accounts
        if entry.username == "admin" and entry.is_compromised:
            vulnerability_score *= 2

print(f"Result: {vulnerability_score}")