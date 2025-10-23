#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <memory>

class PixelRegion {
private:
    std::vector<int> intensities;

public:
    explicit PixelRegion(std::vector<int> vals) : intensities(std::move(vals)) {}
    
    double mean() const {
        long long sum = 0;
        for (int val : intensities) sum += val;
        return static_cast<double>(sum) / intensities.size();
    }
    
    double variance() const {
        double m = mean();
        double var_sum = 0;
        for (int val : intensities) {
            var_sum += (val - m) * (val - m);
        }
        return var_sum / intensities.size();
    }
};

constexpr double threshold_factor = 1.5;

constexpr double adjusted_threshold(double base, double factor) {
    return base * factor;
}

int main() {
    auto region = std::make_unique<PixelRegion>(std::vector<int>{100, 102, 98, 105, 97, 103, 99, 101, 104, 96});
    
    double mean_intensity = region->mean();
    double variance_val = region->variance();
    double std_dev = sqrt(variance_val);
    
    bool is_high_variance = std_dev > 2.0;
    double baseline = is_high_variance ? std_dev : mean_intensity * 0.1;
    
    double threshold = adjusted_threshold(baseline, threshold_factor);
    int outlier_count = 0;
    
    for (int pixel : {110, 90, 108, 95}) {
        if (std::abs(pixel - mean_intensity) > threshold) {
            outlier_count++;
        }
    }
    
    double anomaly_score = (outlier_count > 1) ? (outlier_count * std_dev) : (mean_intensity / (std_dev + 1));
    
    std::cout << "Result: " << static_cast<int>(anomaly_score) << std::endl;
    return 0;
}