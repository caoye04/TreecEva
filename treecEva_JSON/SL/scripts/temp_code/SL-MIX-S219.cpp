#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>

struct Package {
    int weight;
    int value;
};

template<typename T>
class KnapsackOptimizer {
private:
    std::vector<T> items;
    int capacity;

public:
    KnapsackOptimizer(int cap) : capacity(cap) {}
    
    void addItem(const T& item) {
        items.push_back(item);
    }
    
    int optimize() {
        int n = items.size();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(capacity + 1, 0));
        
        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (items[i-1].weight <= w) {
                    dp[i][w] = std::max(dp[i-1][w], dp[i-1][w - items[i-1].weight] + items[i-1].value);
                } else {
                    dp[i][w] = dp[i-1][w];
                }
            }
        }
        
        return dp[n][capacity];
    }
};

int main() {
    const int truckCapacity = 10;
    auto optimizer = std::make_unique<KnapsackOptimizer<Package>>(truckCapacity);
    
    optimizer->addItem({2, 3});
    optimizer->addItem({3, 4});
    optimizer->addItem({4, 5});
    optimizer->addItem({5, 6});
    
    int maxValueLoaded = optimizer->optimize();
    
    std::cout << "Result: " << maxValueLoaded << std::endl;
    return 0;
}