#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <queue>
#include <memory>
#include <algorithm>

using namespace std;

int main() {
    // Container IDs and weights
    vector<int> container_ids = {101, 202, 303, 404};
    vector<int> container_weights = {150, 200, 175, 225};
    
    // Priority queue for weights (max heap)
    priority_queue<int> weight_queue;
    for (int weight : container_weights) {
        weight_queue.push(weight);
    }
    
    // Dynamic programming table for checksum calculation
    unique_ptr<vector<int>> dp = make_unique<vector<int>>(container_ids.size() + 1, 0);
    
    // Calculate checksum using dynamic programming
    for (size_t i = 1; i <= container_ids.size(); ++i) {
        int id_digit_sum = 0;
        int temp_id = container_ids[i-1];
        while (temp_id > 0) {
            id_digit_sum += temp_id % 10;
            temp_id /= 10;
        }
        
        // Nested loop for additional processing
        int adjustment = 0;
        for (int j = 0; j < id_digit_sum; ++j) {
            if (j % 2 == 0) {
                adjustment += 1;
            } else {
                adjustment -= 1;
            }
        }
        
        (*dp)[i] = (*dp)[i-1] + id_digit_sum + adjustment;
    }
    
    // Apply weight-based modifier
    int weight_modifier = weight_queue.top();
    weight_queue.pop();
    
    int final_checksum = (*dp)[container_ids.size()] + (weight_modifier % 10);
    
    cout << "Result: " << final_checksum << endl;
    return 0;
}