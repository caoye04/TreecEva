import re
from functools import reduce

def calculate_risk_factor(amount):
    return round(amount ** 0.5, 2)

def is_suspicious(patterns, description):
    return any(re.search(pattern, description, re.IGNORECASE) for pattern in patterns)

# Transaction data
transaction_amounts = [1200.50, 2500.75, 999.99, 5000.00, 100.25]
transaction_descriptions = [
    "Standard wire transfer",
    "Urgent money transfer to offshore account",
    "Regular payment for services",
    "Crypto conversion fee",
    "Refund for returned item"
]

# Compliance parameters
suspicious_patterns = [r'offshore', r'crypto', r'urgent']
sensitivity_factor = 1.75
base_compliance_points = 100

# Processing logic
risk_factors = list(map(calculate_risk_factor, transaction_amounts))
suspicious_flags = list(map(lambda desc: is_suspicious(suspicious_patterns, desc), transaction_descriptions))

weighted_risks = [rf * sensitivity_factor if flag else rf for rf, flag in zip(risk_factors, suspicious_flags)]
total_risk = reduce(lambda x, y: x + y, weighted_risks)

# Final compliance score calculation
compliance_score = int(base_compliance_points - total_risk) if total_risk > 50 else base_compliance_points

print(f"Result: {compliance_score}")