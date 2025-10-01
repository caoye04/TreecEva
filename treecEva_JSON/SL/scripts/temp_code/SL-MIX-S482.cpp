#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <map>

double compute_recursive_power_sum(int base, int depth) {
    if (depth <= 0) return 1.0;
    return pow(base, depth) + compute_recursive_power_sum(base, depth - 1);
}

struct DataProcessor {
    std::vector<std::vector<int>> matrix;
    std::map<int, double> lookup_table;
    
    void initialize() {
        matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
        for (const auto& row : matrix) {
            for (int val : row) {
                lookup_table[val] = sqrt(val) * log(val);
            }
        }
    }
    
    double aggregate_values(bool use_lookup) {
        double sum = 0.0;
        for (size_t i = 0; i < matrix.size(); ++i) {
            for (size_t j = 0; j < matrix[i].size(); ++j) {
                int current = matrix[i][j];
                if (use_lookup && lookup_table.find(current) != lookup_table.end()) {
                    sum += lookup_table[current];
                } else {
                    sum += compute_recursive_power_sum(current % 10, 3);
                }
            }
        }
        return sum;
    }
};

int main() {
    DataProcessor processor;
    processor.initialize();
    
    double intermediate = processor.aggregate_values(true);
    int selector = static_cast<int>(intermediate) % 4;
    
    double adjustment = 0.0;
    switch(selector) {
        case 0:
            adjustment = sin(intermediate / 100.0);
            break;
        case 1:
            adjustment = cos(intermediate / 100.0);
            break;
        case 2:
            adjustment = tan(intermediate / 100.0);
            break;
        default:
            adjustment = atan(intermediate / 100.0);
    }
    
    double final_result = floor(intermediate + adjustment * 1000);
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}