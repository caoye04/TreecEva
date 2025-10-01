#define M_PI 3.14159265358979323846
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
    map<string, vector<double>> data_map;
    data_map["alpha"] = {2.5, 3.0, 1.5};
    data_map["beta"] = {4.0, 2.0, 0.5};
    data_map["gamma"] = {1.0, 2.0, 3.0};
    
    double accumulator = 0.0;
    int operation_selector = 0;
    
    for (const auto& entry : data_map) {
        const vector<double>& values = entry.second;
        double intermediate = 0.0;
        
        for (size_t i = 0; i < values.size(); ++i) {
            double val = values[i];
            if (i == 0) {
                intermediate = val;
            } else {
                intermediate = compute_expression(intermediate, val, operation_selector);
            }
        }
        
        if (entry.first == "beta") {
            intermediate = ceil(intermediate);
        }
        
        accumulator += intermediate;
        operation_selector = (operation_selector + 1) % 4;
    }
    
    // Perform bitwise operations on the integer part of accumulator
    int int_part = static_cast<int>(accumulator);
    int_part = (int_part << 2) ^ 0xF;
    
    // Final calculation involving trigonometric functions
    double fractional_part = accumulator - static_cast<int>(accumulator);
    double trig_result = tan(fractional_part * M_PI);
    
    // Combine results
    double final_result = int_part + trig_result;
    
    // Apply final transformation
    final_result = round(final_result * 1000.0) / 1000.0;
    
    cout << "Result: " << final_result << endl;
    return 0;
}