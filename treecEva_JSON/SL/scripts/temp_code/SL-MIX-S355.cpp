#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

class TransactionToken {
public:
    std::string token;
    TransactionToken(std::string t) : token(std::move(t)) {}
    TransactionToken(TransactionToken&& other) noexcept : token(std::move(other.token)) {}
    TransactionToken(const TransactionToken&) = delete;
};

int main() {
    std::vector<TransactionToken> tokens;
    tokens.emplace_back(TransactionToken("TX001"));
    tokens.emplace_back(TransactionToken("TX002"));
    tokens.emplace_back(TransactionToken("TX003"));
    
    int verificationChecksum = 0;
    int multiplier = 1;
    
    for (auto& tokenObj : tokens) {
        std::string token = tokenObj.token;
        std::string code = token.substr(2, 3);
        int numericCode = std::stoi(code);
        
        switch (numericCode % 5) {
            case 0:
                verificationChecksum += numericCode * 2;
                break;
            case 1:
                verificationChecksum -= numericCode;
                break;
            case 2:
                verificationChecksum += static_cast<int>(std::pow(numericCode, 1.5));
                break;
            case 3:
                verificationChecksum ^= numericCode;
                break;
            case 4:
                verificationChecksum += numericCode * multiplier;
                multiplier++;
                break;
        }
    }
    
    std::cout << "Result: " << verificationChecksum << std::endl;
    return 0;
}