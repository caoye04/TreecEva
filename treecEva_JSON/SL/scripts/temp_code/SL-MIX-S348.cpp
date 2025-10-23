#define _USE_MATH_DEFINES
#include <iostream>
#include <stack>
#include <queue>
#include <cmath>
#include <vector>

template<typename T>
class VolatilityTracker {
private:
    std::stack<T> volatility_stack;
    std::queue<T> alert_queue;
    int max_history;

public:
    VolatilityTracker(int history) : max_history(history) {}
    
    T compute_next_volatility(T a, T b) {
        return std::sqrt(a*a + b*b);
    }
    
    void add_volatility(T value) {
        volatility_stack.push(value);
        if (volatility_stack.size() > max_history) {
            volatility_stack.pop();
        }
        
        if (value > 3.0) {
            alert_queue.push(value);
        }
    }
    
    T get_latest() {
        return volatility_stack.top();
    }
    
    size_t alert_count() {
        return alert_queue.size();
    }
};

int main() {
    VolatilityTracker<double> tracker(5);
    std::vector<double> initial_values = {1.0, 2.0};
    
    // Initialize with first two values
    tracker.add_volatility(initial_values[0]);
    tracker.add_volatility(initial_values[1]);
    
    // Generate next 5 values in modified Fibonacci sequence
    for (int i = 0; i < 5; ++i) {
        double a = initial_values[i];
        double b = initial_values[i+1];
        double next = tracker.compute_next_volatility(a, b);
        initial_values.push_back(next);
        tracker.add_volatility(next);
    }
    
    double latest_volatility = tracker.get_latest();
    std::cout << "Result: " << latest_volatility << std::endl;
    return 0;
}