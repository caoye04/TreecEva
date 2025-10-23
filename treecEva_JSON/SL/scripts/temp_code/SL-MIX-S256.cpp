#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

struct Vertex {
    double x, y, z;
    Vertex(double x_, double y_, double z_) : x(x_), y(y_), z(z_) {}
};

double computeDistance(const Vertex& a, const Vertex& b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2) + pow(a.z - b.z, 2));
}

int main() {
    std::vector<Vertex> mesh_vertices = {
        Vertex(0.0, 0.0, 0.0),
        Vertex(3.0, 4.0, 0.0),
        Vertex(0.0, 0.0, 5.0),
        Vertex(1.0, 1.0, 1.0)
    };
    
    double total_cost = 0.0;
    size_t n = mesh_vertices.size();
    
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = i + 1; j < n; ++j) {
            double dist = computeDistance(mesh_vertices[i], mesh_vertices[j]);
            total_cost += log10(dist + 1.0);
        }
    }
    
    double avg_cost = total_cost / (n * (n - 1) / 2);
    
    double greedy_improvement = 0.0;
    for (const auto& v : mesh_vertices) {
        double penalty = pow(v.x, 2) + pow(v.y, 2) + pow(v.z, 2);
        greedy_improvement += penalty * exp(-avg_cost);
    }
    
    double final_adjustment = round(greedy_improvement * 1000.0) / 1000.0;
    
    std::cout << "Result: " << final_adjustment << std::endl;
    return 0;
}