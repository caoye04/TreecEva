#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <memory>
#include <optional>

class AuthToken {
public:
    int priority;
    int value;
    AuthToken(int p, int v) : priority(p), value(v) {}
};

struct Compare {
    bool operator()(const std::shared_ptr<AuthToken>& a, const std::shared_ptr<AuthToken>& b) {
        return a->priority < b->priority;
    }
};

int main() {
    std::priority_queue<std::shared_ptr<AuthToken>, std::vector<std::shared_ptr<AuthToken>>, Compare> token_queue;
    
    // Initialize tokens
    token_queue.push(std::make_shared<AuthToken>(3, 100));
    token_queue.push(std::make_shared<AuthToken>(1, 50));
    token_queue.push(std::make_shared<AuthToken>(2, 75));
    
    int accumulator = 0;
    std::optional<int> modifier = std::nullopt;
    
    // Process tokens
    while (!token_queue.empty()) {
        auto token = token_queue.top();
        token_queue.pop();
        
        // Apply modular arithmetic
        int processed_value = (token->value * 3) % 256;
        
        // Short-circuit evaluation
        if (token->priority > 1 && (processed_value > 100 || token->value < 60)) {
            if (!modifier.has_value() || processed_value > modifier.value()) {
                modifier = processed_value;
            }
        }
        
        accumulator += processed_value;
    }
    
    int authentication_result = 0;
    
    // Final computation
    if (modifier.has_value() && accumulator > 200) {
        authentication_result = (accumulator + modifier.value()) % 1000;
    } else {
        authentication_result = accumulator % 1000;
    }
    
    std::cout << "Result: " << authentication_result << std::endl;
    return 0;
}