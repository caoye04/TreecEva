#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <algorithm>
#include <memory>

int calculate_median(std::vector<int> data) {
    std::sort(data.begin(), data.end());
    size_t n = data.size();
    if (n % 2 == 0) {
        return (data[n/2 - 1] + data[n/2]) / 2;
    } else {
        return data[n/2];
    }
}

int main() {
    std::string transaction_log = "TXN:200|TXN:150|TXN:300|TXN:250|TXN:100";
    std::regex pattern("TXN:(\\d+)");
    std::sregex_iterator iter(transaction_log.begin(), transaction_log.end(), pattern);
    std::sregex_iterator end;
    
    std::vector<int> amounts;
    for (; iter != end; ++iter) {
        amounts.push_back(std::stoi((*iter)[1]));
    }
    
    int median_amount = calculate_median(amounts);
    
    std::unique_ptr<std::vector<int>> deviations(new std::vector<int>());
    for (int amount : amounts) {
        deviations->push_back(abs(amount - median_amount));
    }
    
    int total_deviation = 0;
    for (int dev : *deviations) {
        total_deviation += dev;
    }
    
    bool has_high_deviation = false;
    for (int dev : *deviations) {
        if (dev > 75) {
            has_high_deviation = true;
            break;
        }
    }
    
    int anomaly_score = 0;
    if (has_high_deviation && total_deviation > 200) {
        anomaly_score = 10;
    } else if (has_high_deviation || total_deviation > 150) {
        anomaly_score = 5;
    } else {
        anomaly_score = 0;
    }
    
    std::cout << "Result: " << anomaly_score << std::endl;
    return 0;
}