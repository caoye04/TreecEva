#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

template<typename T>
class PortfolioAdjuster {
private:
    vector<T> weights;
    vector<T> projections;

public:
    PortfolioAdjuster(vector<T> w, vector<T> p) : weights(move(w)), projections(move(p)) {}
    
    T compute_adjustment() {
        T adjustment = 0;
        bool high_risk_flag = false;
        
        for(size_t i = 0; i < weights.size(); ++i) {
            T delta = projections[i] - weights[i];
            
            // Greedy selection with early pruning
            if(delta > 0.1 && (weights[i] < 0.3 || high_risk_flag)) {
                adjustment += delta * 2;
                if(adjustment > 1.0) { high_risk_flag = true; }
            } else if(delta < -0.05 && weights[i] > 0.1) {
                adjustment += delta;
                if(adjustment < -0.5) { break; }
            }
            
            // Short-circuit evaluation for risk management
            if(high_risk_flag && adjustment > 0.8 && i < weights.size()/2) {
                return adjustment * (i % 3 ? 1.5 : 2.0);
            }
        }
        
        // Ternary-based final calibration
        return (adjustment > 0) ? adjustment * 1.2 : adjustment * 0.8;
    }
};

int main() {
    vector<double> initial_weights = {0.25, 0.35, 0.15, 0.25};
    vector<double> market_projections = {0.30, 0.40, 0.10, 0.20};
    
    PortfolioAdjuster<double> adjuster(initial_weights, market_projections);
    double final_adjustment = adjuster.compute_adjustment();
    
    cout << "Result: " << final_adjustment << endl;
    return 0;
}