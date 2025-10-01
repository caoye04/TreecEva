#define _USE_MATH_DEFINES
#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <string>

class DataProcessor {
private:
    std::map<std::string, std::vector<int>> data_map;
    std::map<std::string, double> calc_map;

public:
    void initialize() {
        data_map["alpha"] = {3, 5, 7, 11};
        data_map["beta"] = {2, 4, 6, 8, 10};
        data_map["gamma"] = {1, 3, 5, 7, 9, 11};
    }

    void process() {
        for (auto& entry : data_map) {
            double sum = 0;
            int count = 0;
            for (int val : entry.second) {
                sum += std::pow(val, 2);
                count++;
            }
            calc_map[entry.first] = sum / count;
        }
    }

    double aggregate() {
        double product = 1.0;
        for (const auto& entry : calc_map) {
            product *= entry.second;
        }
        return std::sqrt(product);
    }

    int complex_operation() {
        int xor_result = 0;
        for (const auto& entry : data_map) {
            for (int val : entry.second) {
                xor_result ^= (val << 1);
            }
        }
        return xor_result & 0xFF;
    }
};

int main() {
    DataProcessor processor;
    processor.initialize();
    processor.process();
    
    double agg_value = processor.aggregate();
    int xor_val = processor.complex_operation();
    
    int final_result = static_cast<int>(agg_value) ^ xor_val;
    final_result = (final_result * 17) % 1000;
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}