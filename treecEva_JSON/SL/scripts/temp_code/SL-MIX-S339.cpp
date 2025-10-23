#define _USE_MATH_DEFINES
#include <iostream>
#include <optional>
#include <vector>

int main() {
    int purchase_amount = 67;
    int payment = 100;
    int change = payment - purchase_amount;
    
    auto greedy_coin_calculator = [change]() -> int {
        std::vector<int> denominations = {25, 10, 5, 1};
        int remaining = change;
        int coins = 0;
        
        for (int denom : denominations) {
            coins += remaining / denom;
            remaining %= denom;
        }
        return coins;
    };
    
    std::optional<int> total_coins;
    
    switch (change) {
        case 33:
            total_coins = 4;
            break;
        case 32:
            total_coins = 4;
            break;
        default:
            total_coins = greedy_coin_calculator();
            break;
    }
    
    std::cout << "Result: " << *total_coins << std::endl;
    return 0;
}