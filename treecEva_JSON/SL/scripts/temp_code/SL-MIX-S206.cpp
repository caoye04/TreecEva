#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <cmath>

class HashTransformer {
private:
    double accumulatedValue;

public:
    HashTransformer() : accumulatedValue(0.0) {}
    
    HashTransformer& operator<<(const std::string& input) {
        for (size_t i = 0; i < input.length(); ++i) {
            double charValue = static_cast<double>(input[i]);
            double poweredValue = pow(charValue, i+1);
            accumulatedValue += log(poweredValue + 1.0);
        }
        return *this;
    }
    
    HashTransformer& operator>>(double& output) {
        output = accumulatedValue;
        return *this;
    }
    
    double getValue() const { return accumulatedValue; }
};

int main() {
    HashTransformer hasher;
    std::string secret = "CODE";
    double transformedHash = 0.0;
    
    hasher << secret;
    hasher >> transformedHash;
    
    // Additional transformation step
    int charCount = secret.length();
    transformedHash = pow(transformedHash, 1.0/charCount) * tgamma(charCount+1); // tgamma(n+1) = n!
    
    std::cout << "Result: " << static_cast<long long>(transformedHash) << std::endl;
    return 0;
}