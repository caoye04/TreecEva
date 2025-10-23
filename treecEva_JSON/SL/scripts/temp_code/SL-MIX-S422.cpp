#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <unordered_map>
#include <memory>
#include <vector>

using namespace std;

// String hashing function
size_t hash_string(const string& s) {
    size_t hash = 0;
    for (char c : s) {
        hash = hash * 31 + c;
    }
    return hash;
}

// Memoization table for dynamic programming
unordered_map<string, int> memo;

// Recursive backtracking function with memoization
int calculate_loading_efficiency(const vector<string>& packages, int index, int current_load) {
    // Base case
    if (index >= packages.size()) {
        return current_load;
    }
    
    // Create key for memoization
    string key = to_string(index) + "," + to_string(current_load);
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }
    
    // Get hash of current package
    size_t package_hash = hash_string(packages[index]);
    
    // Apply encoding/decoding transformation
    int encoded_value = (package_hash & 0xFF) ^ ((package_hash >> 8) & 0xFF);
    
    // Use ternary operator and short-circuit evaluation
    bool is_heavy = (encoded_value > 100) && (packages[index].length() > 3);
    int weight_factor = is_heavy ? 2 : 1;
    
    // Recursive calls with move semantics for efficiency
    int include_package = calculate_loading_efficiency(
        move(packages), index + 1, current_load + (encoded_value * weight_factor)
    );
    
    int exclude_package = calculate_loading_efficiency(
        move(packages), index + 1, current_load
    );
    
    // Store result in memo table
    return memo[key] = max(include_package, exclude_package);
}

int main() {
    // Define package sequence
    vector<string> shipment_packages = {"BOX-A", "CYL-B", "SPH-C", "CUB-D", "IRG-E"};
    
    // Use smart pointer for resource management
    unique_ptr<int> efficiency_score = make_unique<int>(0);
    
    // Calculate loading efficiency using dynamic programming
    *efficiency_score = calculate_loading_efficiency(shipment_packages, 0, 0);
    
    // Apply final adjustment using bitwise operations
    int final_loading_score = (*efficiency_score & 0x1FF) | ((*efficiency_score >> 9) & 0x3F);
    
    cout << "Result: " << final_loading_score << endl;
    
    return 0;
}