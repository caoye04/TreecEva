#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <regex>
#include <memory>
#include <cmath>

class TransactionProcessor {
private:
    std::vector<double> amounts;
    std::vector<std::string> categories;

public:
    TransactionProcessor(std::vector<double> a, std::vector<std::string> c) : amounts(a), categories(c) {}
    
    double process() {
        double baseBalance = 1000.0;
        std::regex depositPattern("DEP[0-9]+", std::regex_constants::icase);
        std::regex withdrawalPattern("WTH[0-9]+", std::regex_constants::icase);
        
        auto adjustAmount = [](double amount, const std::string& category) -> double {
            if (category.find("PREMIUM") != std::string::npos) {
                return amount * 1.05;
            }
            return amount;
        };
        
        for (size_t i = 0; i < amounts.size(); ++i) {
            double adjustedAmount = adjustAmount(amounts[i], categories[i]);
            if (std::regex_match(categories[i], depositPattern)) {
                baseBalance += adjustedAmount;
            } else if (std::regex_match(categories[i], withdrawalPattern)) {
                baseBalance -= adjustedAmount;
            } else {
                baseBalance += (adjustedAmount > 100) ? adjustedAmount * 0.01 : 0;
            }
        }
        
        // Statistical adjustment: mean of top 3 transactions
        std::vector<double> sortedAmounts = amounts;
        std::sort(sortedAmounts.begin(), sortedAmounts.end(), std::greater<double>());
        double meanTop3 = (sortedAmounts[0] + sortedAmounts[1] + sortedAmounts[2]) / 3.0;
        
        return baseBalance + (meanTop3 > 200 ? meanTop3 * 0.02 : 0);
    }
};

int main() {
    std::vector<double> transactionAmounts = {250.0, 150.0, 300.0, 75.0, 500.0};
    std::vector<std::string> transactionCategories = {"DEP101", "WTH202", "DEPPREMIUM303", "FEE001", "DEP404"};
    
    std::unique_ptr<TransactionProcessor> processor = std::make_unique<TransactionProcessor>(transactionAmounts, transactionCategories);
    double adjustedBalance = processor->process();
    
    std::cout << "Result: " << adjustedBalance << std::endl;
    return 0;
}