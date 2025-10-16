#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

int main() {
    // Simulated daily volatility data
    std::vector<int> daily_volatility = {45, 23, 67, 12, 89, 34, 78, 56, 90, 11};
    
    // Min-heap to track lowest volatility values
    std::priority_queue<int, std::vector<int>, std::greater<int>> volatility_min_heap;
    
    // Insert all volatility data into the heap
    for (int vol : daily_volatility) {
        volatility_min_heap.push(vol);
    }
    
    // Extract the three smallest volatility values
    int sum_lowest_vols = 0;
    for (int i = 0; i < 3; ++i) {
        sum_lowest_vols += volatility_min_heap.top();
        volatility_min_heap.pop();
    }
    
    // Thresholds for risk categorization (must be sorted for binary search)
    std::vector<int> risk_thresholds = {20, 40, 60, 80, 100};
    
    // Binary search for the risk category
    int risk_category_index = -1;
    int left = 0;
    int right = risk_thresholds.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (risk_thresholds[mid] >= sum_lowest_vols) {
            risk_category_index = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    std::cout << "Result: " << risk_category_index << std::endl;
    return 0;
}