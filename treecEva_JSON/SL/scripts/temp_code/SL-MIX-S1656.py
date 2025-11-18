import hashlib

event_log = [
    "USER_LOGIN",
    "FILE_ACCESS",
    "PRIVILEGE_ESCALATION",
    "NETWORK_CONNECTION",
    "DATA_EXFILTRATION"
]

def hash_event(event_str):
    return int(hashlib.md5(event_str.encode()).hexdigest(), 16) % 1000

class IntrusionDetector:
    def __init__(self):
        self.state = 'IDLE'
        self.intrusion_score = 0
        self.transition_history = []
    
    def process_event(self, event):
        event_hash = hash_event(event)
        # State transition logic
        if self.state == 'IDLE':
            if event_hash > 500:
                self.state = 'SUSPICIOUS_ACTIVITY'
                self.intrusion_score += 10
            else:
                self.state = 'NORMAL'
                self.intrusion_score += 1
        elif self.state == 'NORMAL':
            if event_hash % 7 == 0:
                self.state = 'SUSPICIOUS_ACTIVITY'
                self.intrusion_score += 15
            elif event_hash % 3 == 0:
                self.state = 'MONITORING'
                self.intrusion_score += 3
            else:
                self.intrusion_score += 1
        elif self.state == 'SUSPICIOUS_ACTIVITY':
            if event_hash < 200:
                self.state = 'ALERT'
                self.intrusion_score += 50
            elif event_hash % 5 == 0:
                self.state = 'INVESTIGATING'
                self.intrusion_score += 25
            else:
                self.intrusion_score += 5
        elif self.state == 'MONITORING':
            if event_hash > 800:
                self.state = 'SUSPICIOUS_ACTIVITY'
                self.intrusion_score += 10
            else:
                self.intrusion_score += 2
        elif self.state == 'INVESTIGATING':
            if not (event_hash % 2 == 0):  # Odd hash
                self.state = 'ALERT'
                self.intrusion_score += 30
            else:
                self.state = 'NORMAL'
                self.intrusion_score -= 5
        elif self.state == 'ALERT':
            self.intrusion_score += 5  # Persistent threat score
        
        self.transition_history.append((event, self.state))

detector = IntrusionDetector()

# Process all events
for event in event_log:
    detector.process_event(event)

print(f"Result: {detector.intrusion_score}")