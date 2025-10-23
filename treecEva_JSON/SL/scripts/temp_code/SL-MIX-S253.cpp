#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    priority_queue<int> peak_rates;
    stack<int> transaction_stack;
    vector<int> exchange_rates = {7, 2, 9, 1, 5, 6, 3, 8, 4};
    int validated_trades = 0;
    
    // Populate peak rates heap
    for (int rate : exchange_rates) {
        peak_rates.push(rate);
    }
    
    // Process transactions with stack
    for (int i = 0; i < exchange_rates.size(); ++i) {
        if (exchange_rates[i] > 4) {
            transaction_stack.push(exchange_rates[i]);
        }
    }
    
    // Validate trades
    while (!transaction_stack.empty()) {
        int current_transaction = transaction_stack.top();
        transaction_stack.pop();
        
        if (!peak_rates.empty() && current_transaction == peak_rates.top()) {
            validated_trades += current_transaction;
            peak_rates.pop();
        } else if (current_transaction < 7) {
            break;
        }
    }
    
    cout << "Result: " << validated_trades << endl;
    return 0;
}