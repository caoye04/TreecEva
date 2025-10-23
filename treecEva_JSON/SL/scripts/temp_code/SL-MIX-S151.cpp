#define _USE_MATH_DEFINES
#include <iostream>
#include <regex>
#include <string>
#include <cmath>

template<typename T>
class TaxCalculator {
public:
    static T calculate(T base, T rate) {
        return base * (1.0 + rate);
    }
};

template<>
class TaxCalculator<int> {
public:
    static int calculate(int base, int rate_percentage) {
        return base + (base * rate_percentage / 100);
    }
};

int main() {
    std::string logEntry = "TXN:2023-09-30T15:30:00Z|USD|AMOUNT:1250.75|FEE:30";
    std::regex amountPattern(R"(AMOUNT:(\d+\.\d+))");
    std::smatch matches;
    double extractedValue = 0.0;
    
    if (std::regex_search(logEntry, matches, amountPattern)) {
        extractedValue = std::stod(matches[1].str());
    }
    
    // Apply a 7.5% tax using the specialized calculator for precision
    double taxedValue = TaxCalculator<double>::calculate(extractedValue, 0.075);
    
    // Simulate a discount encoded as a bitmask operation
    int discountCode = 0b1010; // Represents a 10% discount in binary flags
    int mask = 0xF;            // Mask to isolate lower 4 bits
    int effectiveDiscount = discountCode & mask;
    
    // Convert percentage discount to a multiplier
    double discountMultiplier = 1.0 - (effectiveDiscount / 100.0);
    
    // Apply discount
    double discountedValue = taxedValue * discountMultiplier;
    
    // Round to nearest cent
    double roundedValue = std::round(discountedValue * 100.0) / 100.0;
    
    // Final adjustment using bit shifting for scaling
    int scaledAmount = static_cast<int>(roundedValue * 100); // Convert to cents
    scaledAmount >>= 2; // Divide by 4 using right shift
    
    double adjustedAmount = scaledAmount / 25.0; // Re-scale to original unit
    
    //QUERY_POINT
    std::cout << "Result: " << adjustedAmount << std::endl;
    return 0;
}