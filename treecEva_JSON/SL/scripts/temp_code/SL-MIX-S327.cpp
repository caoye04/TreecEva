#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>

template <typename T>
class RiskEngine {
private:
    int currentState;
    T riskMetric;

public:
    RiskEngine(T initialRisk) : currentState(0), riskMetric(initialRisk) {}
    
    void processEvent(double delta) {
        bool isSignificant = std::abs(delta) > 5.0;
        
        // State transition logic
        if (currentState == 0) {
            currentState = isSignificant ? 1 : 0;
        } else if (currentState == 1) {
            currentState = (delta < -10.0) ? 2 : (isSignificant ? 1 : 0);
        } else {
            currentState = (delta > 0) ? 1 : 2;
        }
        
        // Risk calculation based on state and delta
        switch(currentState) {
            case 0: // STABLE
                riskMetric += delta * 0.1;
                break;
            case 1: // VOLATILE
                riskMetric = riskMetric * (1.0 + delta/100.0);
                if (delta > 15.0) return; // Early return
                break;
            case 2: // CRASHING
                riskMetric -= std::pow(std::abs(delta), 0.5);
                if (riskMetric < 0) { riskMetric = 0; break; }
                break;
        }
        
        // Additional risk adjustment
        riskMetric = (riskMetric > 50.0) ? riskMetric * 0.95 : riskMetric;
    }
    
    T getRiskMetric() const { return riskMetric; }
};

int main() {
    std::vector<double> priceChanges = {3.2, -7.1, 12.5, -15.3, 4.8, -22.1, 6.7};
    RiskEngine<double> engine(10.0);
    
    for (const auto& change : priceChanges) {
        engine.processEvent(change);
    }
    
    double finalRisk = engine.getRiskMetric();
    std::cout << "Result: " << finalRisk << std::endl;
    return 0;
}