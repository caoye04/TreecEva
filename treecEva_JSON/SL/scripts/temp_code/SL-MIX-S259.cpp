#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>

class VendingMachine {
public:
    struct Change {
        int quarters = 0;
        int dimes = 0;
        int nickels = 0;
        int pennies = 0;
    };

    constexpr static Change calculateChange(int amount) {
        Change change;
        change.quarters = amount / 25;
        amount %= 25;
        change.dimes = amount / 10;
        amount %= 10;
        change.nickels = amount / 5;
        amount %= 5;
        change.pennies = amount;
        return change;
    }
};

enum class TransactionState {
    START,
    PROCESSING,
    VALIDATING,
    COMPLETED
};

int main() {
    const int item_price = 87;
    const int customer_payment = 100;
    const int change_amount = customer_payment - item_price;
    
    auto change = std::make_unique<VendingMachine::Change>(
        VendingMachine::calculateChange(change_amount)
    );
    
    TransactionState state = TransactionState::START;
    
    // State machine validation
    if (state == TransactionState::START) {
        state = TransactionState::PROCESSING;
    }
    
    if (state == TransactionState::PROCESSING) {
        state = TransactionState::VALIDATING;
    }
    
    if (state == TransactionState::VALIDATING) {
        state = TransactionState::COMPLETED;
    }
    
    int nickel_count = 0;
    if (state == TransactionState::COMPLETED) {
        nickel_count = change->nickels;
    }
    
    std::cout << "Result: " << nickel_count << std::endl;
    return 0;
}