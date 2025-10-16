#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <optional>
#include <algorithm>

struct Transaction {
    int value;
    int cost;
    unsigned char flags;
};

bool is_valid_bundle(const std::vector<Transaction>& transactions, int index, unsigned char required_flags) {
    if (index < 0 || index >= transactions.size()) return false;
    return (transactions[index].flags & required_flags) == required_flags;
}

int main() {
    std::vector<Transaction> portfolio = {
        {100, 50, 0b00000110},
        {200, 100, 0b00000011},
        {150, 75, 0b00000101},
        {300, 150, 0b00000111},
        {250, 125, 0b00000010}
    };

    unsigned char mandatory_flags = 0b00000010;
    int budget = 300;
    int total_spent = 0;
    int final_bundle_value = 0;

    // Sort by value-to-cost ratio descending (greedy)
    std::sort(portfolio.begin(), portfolio.end(), [](const Transaction& a, const Transaction& b) {
        return (double)a.value / a.cost > (double)b.value / b.cost;
    });

    for (int i = 0; i < portfolio.size(); ++i) {
        bool flag_check = is_valid_bundle(portfolio, i, mandatory_flags);
        bool budget_check = (total_spent + portfolio[i].cost <= budget);
        
        if (flag_check && budget_check) {
            total_spent += portfolio[i].cost;
            final_bundle_value += portfolio[i].value;
        }
        else if (!flag_check && budget_check && (portfolio[i].flags & 0b00000100)) {
            // Alternative condition for special flag
            total_spent += portfolio[i].cost / 2;
            final_bundle_value += portfolio[i].value / 2;
        }
    }

    // Adjust final value based on leftover budget (bitwise operation)
    if ((budget - total_spent) & 0b00000001) {
        final_bundle_value += 10; // Odd leftover bonus
    }

    std::cout << "Result: " << final_bundle_value << std::endl;
    return 0;
}