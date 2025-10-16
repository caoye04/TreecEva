#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>

struct Transaction {
    std::string id;
    double amount;
    bool is_verified;
};

// Custom string hash function
uint32_t hash_string(const std::string& str) {
    uint32_t hash = 0;
    for (char c : str) {
        hash = hash * 31 + c;
    }
    return hash;
}

int main() {
    std::vector<Transaction> ledger = {
        {"TX001", 1250.75, true},
        {"TX002", 89.99, false},
        {"TX003", 5000.00, true},
        {"TX004", 25.30, true},
        {"TX005", 10000.00, false}
    };
    
    // Lambda to check if transaction needs manual review
    auto needs_review = [](const Transaction& t) -> bool {
        bool high_value = t.amount > 1000.0;
        bool unverified = !t.is_verified;
        bool hash_check = (hash_string(t.id) % 100) > 50;
        return (high_value && unverified) || hash_check;
    };
    
    // Sort by amount descending
    std::sort(ledger.begin(), ledger.end(), [](const Transaction& a, const Transaction& b) {
        return a.amount > b.amount;
    });
    
    int flagged_count = 0;
    for (const auto& transaction : ledger) {
        if (needs_review(transaction)) {
            flagged_count++;
        }
    }
    
    std::cout << "Result: " << flagged_count << std::endl;
    return 0;
}