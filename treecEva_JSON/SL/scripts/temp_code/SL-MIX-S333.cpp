#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <memory>

using namespace std;

class Fraction {
public:
    int numerator, denominator;
    
    Fraction(int num = 0, int den = 1) : numerator(num), denominator(den) {}
    
    Fraction operator+(const Fraction& other) const {
        return Fraction(numerator * other.denominator + other.numerator * denominator, 
                        denominator * other.denominator);
    }
    
    Fraction operator*(const Fraction& other) const {
        return Fraction(numerator * other.numerator, 
                        denominator * other.denominator);
    }
    
    bool operator>(const Fraction& other) const {
        return numerator * other.denominator > other.numerator * denominator;
    }
    
    double toDouble() const {
        return static_cast<double>(numerator) / denominator;
    }
};

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int lcm(int a, int int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    // Initialize trajectory parameters
    auto thrustRatio = make_unique<Fraction>(3, 4);
    Fraction velocityFactor(5, 6);
    Fraction gravityAdjustment(7, 9);
    
    // Compute base efficiency
    Fraction baseEfficiency = (*thrustRatio) * velocityFactor;
    
    // Apply gravitational correction
    Fraction correctedEfficiency = baseEfficiency + gravityAdjustment;
    
    // Calculate optimization factors using number theory
    int primeFuelMod = 17;
    int trajectoryGCD = gcd(24, 36);
    int orbitalLCM = lcm(15, 25);
    
    // Compute weighted adjustment factor
    double weightFactor = sin(static_cast<double>(orbitalLCM) / 100.0);
    
    // Apply final adjustments
    bool isEfficient = correctedEfficiency > Fraction(1, 1);
    double efficiencyBoost = isEfficient ? 1.0 + weightFactor : 1.0 - abs(weightFactor);
    
    // Calculate final score
    double rawScore = correctedEfficiency.toDouble() * primeFuelMod * trajectoryGCD;
    double finalEfficiencyScore = rawScore * efficiencyBoost;
    
    cout << "Result: " << finalEfficiencyScore << endl;
    return 0;
}