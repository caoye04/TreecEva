#define _USE_MATH_DEFINES
#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double compute_expression(double a, double b, int op) {
    switch(op) {
        case 0: return pow(a, b);
        case 1: return log(a) / log(b);
        case 2: return sin(a) + cos(b);
        case 3: return floor(a * b);
        default: return a + b;
    }
}

int main() {
    map<string, vector<map<int, double>>> data;
    
    // Initialize data structure
    data["group1"] = vector<map<int, double>>(2);
    data["group1"][0][1] = 3.5;
    data["group1"][0][2] = 4.0;
    data["group1"][1][1] = 2.0;
    data["group1"][1][2] = 3.0;
    
    data["group2"] = vector<map<int, double>>(2);
    data["group2"][0][1] = 5.0;
    data["group2"][0][2] = 2.5;
    data["group2"][1][1] = 1.5;
    data["group2"][1][2] = 6.0;
    
    double accumulator = 0.0;
    int operation_selector = 0;
    
    // Complex nested iteration and calculation
    for (auto& group_pair : data) {
        string group_name = group_pair.first;
        vector<map<int, double>>& group_data = group_pair.second;
        
        for (size_t i = 0; i < group_data.size(); ++i) {
            map<int, double>& inner_map = group_data[i];
            
            double val1 = inner_map[1];
            double val2 = inner_map[2];
            
            double intermediate = compute_expression(val1, val2, operation_selector);
            accumulator += intermediate;
            
            operation_selector = (operation_selector + 1) % 4;
        }
    }
    
    // Bitwise and logical operations
    int mask = 0xF0;  // 240 in decimal
    int value = static_cast<int>(accumulator);
    int masked_value = value & mask;
    bool condition = (masked_value > 100) && (accumulator < 50);
    
    double final_result;
    if (condition) {
        final_result = accumulator * 2.5;
    } else {
        final_result = sqrt(accumulator) + masked_value;
    }
    
    // Final adjustment
    final_result = final_result - (final_result / 3.0);
    
    cout << "Result: " << final_result << endl;
    return 0;
}