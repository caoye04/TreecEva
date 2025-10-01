#define _USE_MATH_DEFINES
#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double compute_expression(double a, double b, int op) {
    switch(op) {
        case 0: return a + b;
        case 1: return a * b;
        case 2: return pow(a, b);
        case 3: return sqrt(abs(a - b));
        default: return 0;
    }
}

int main() {
    map<string, vector<double>> data_map;
    data_map["alpha"] = {2.5, 3.7, 1.2};
    data_map["beta"] = {4.1, 2.8, 5.5};
    data_map["gamma"] = {1.9, 3.3, 2.2};
    
    double accumulator = 0.0;
    int op_index = 0;
    
    for(auto& entry : data_map) {
        vector<double>& vec = entry.second;
        for(size_t i = 0; i < vec.size(); ++i) {
            accumulator = compute_expression(accumulator, vec[i], op_index % 4);
            op_index++;
        }
    }
    
    map<string, map<int, double>> nested_map;
    nested_map["level1"][10] = accumulator;
    nested_map["level1"][20] = accumulator * 1.5;
    nested_map["level2"][30] = accumulator / 2.0;
    nested_map["level2"][40] = pow(accumulator, 1.1);
    
    double intermediate = 0.0;
    for(auto& outer : nested_map) {
        for(auto& inner : outer.second) {
            intermediate += inner.second;
        }
    }
    
    vector<map<string, double>> vec_of_maps(2);
    vec_of_maps[0]["x"] = intermediate;
    vec_of_maps[0]["y"] = intermediate * 0.7;
    vec_of_maps[1]["z"] = intermediate / 1.3;
    vec_of_maps[1]["w"] = sqrt(intermediate);
    
    double final_accumulator = 0.0;
    for(const auto& m : vec_of_maps) {
        for(const auto& pair : m) {
            final_accumulator += pair.second;
        }
    }
    
    int xor_result = 0;
    for(int i = 1; i <= 10; ++i) {
        xor_result ^= i;
    }
    
    double final_result = final_accumulator + xor_result;
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}