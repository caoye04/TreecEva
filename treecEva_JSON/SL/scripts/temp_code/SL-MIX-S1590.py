from functools import reduce

def validate_transaction_stage(stage, amount):
    validators = {
        1: lambda x: x > 100,
        2: lambda x: x % 10 == 0,
        3: lambda x: x < 10000
    }
    return validators.get(stage, lambda x: False)(amount)

def get_tier_multiplier(tier):
    multipliers = {1: 1.02, 2: 1.05, 3: 1.08}
    return multipliers.get(tier, 1.0)

class ConversionProcessor:
    def __init__(self):
        self.state = 'INIT'
        self.conversion_chain = []
    
    def process_amount(self, amount):
        if self.state == 'INIT' and validate_transaction_stage(1, amount):
            self.state = 'TIER_SELECTION'
            tier = 2 if amount > 5000 else 1
            multiplier = get_tier_multiplier(tier)
            adjusted_amount = amount * multiplier
            self.conversion_chain.append(adjusted_amount)
            return adjusted_amount
        elif self.state == 'TIER_SELECTION' and validate_transaction_stage(2, amount):
            self.state = 'VALIDATION_COMPLETE'
            last_value = self.conversion_chain[-1] if self.conversion_chain else 0
            combined = last_value + amount
            self.conversion_chain.append(combined)
            return combined
        elif self.state == 'VALIDATION_COMPLETE' and validate_transaction_stage(3, amount):
            final_adjustment = reduce(lambda acc, x: acc + x * 0.01, self.conversion_chain, 0)
            self.state = 'PROCESSING_COMPLETE'
            return final_adjustment
        return 0

tx_processor = ConversionProcessor()
initial_capital = 2500
interim_deposit = 1200
bonus_injection = 5000

stage_1_result = tx_processor.process_amount(initial_capital)
stage_2_result = tx_processor.process_amount(interim_deposit)
final_conversion_rate = tx_processor.process_amount(bonus_injection)

print(f"Result: {final_conversion_rate}")