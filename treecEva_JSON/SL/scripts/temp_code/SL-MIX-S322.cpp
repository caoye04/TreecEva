#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <functional>

class GridNavigator {
private:
    std::vector<std::vector<int>> grid;
    int max_cost;
    int dest_x, dest_y;
    std::vector<std::pair<int, int>> path;
    std::vector<std::vector<bool>> visited;
    
public:
    GridNavigator(const std::vector<std::vector<int>>& g, int max_c, int dx, int dy)
        : grid(g), max_cost(max_c), dest_x(dx), dest_y(dy) {
        visited.assign(grid.size(), std::vector<bool>(grid[0].size(), false));
    }
    
    // Lambda for movement cost calculation
    auto cost_fn = [](int base_cost, int elevation) -> int {
        return base_cost + (elevation > 0 ? elevation * 2 : 0);
    };
    
    bool find_path(int x, int y, int current_cost) {
        // Early return if out of bounds or already visited
        if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() || visited[x][y])
            return false;
            
        // Check if obstacle
        if (grid[x][y] == -1)
            return false;
            
        // Add current cell to path
        path.push_back({x, y});
        visited[x][y] = true;
        
        // Calculate new cost using lambda
        int new_cost = current_cost + cost_fn(1, grid[x][y]);
        
        // Early return if cost exceeds limit
        if (new_cost > max_cost)
            return false;
            
        // Check if reached destination
        if (x == dest_x && y == dest_y) {
            final_path_cost = new_cost;
            return true;
        }
        
        // Ternary operator to decide whether to continue
        bool should_continue = (new_cost < max_cost/2) ? true : false;
        
        if (should_continue) {
            // Try all four directions
            if (find_path(x+1, y, new_cost) ||  // North
                find_path(x, y+1, new_cost) ||  // East
                find_path(x-1, y, new_cost) ||  // South
                find_path(x, y-1, new_cost)) {  // West
                return true;
            }
        }
        
        // Backtrack
        path.pop_back();
        visited[x][y] = false;
        return false;
    }
    
    int final_path_cost = -1;
};

int main() {
    // Define grid: -1 = obstacle, other values = elevation
    std::vector<std::vector<int>> terrain = {
        { 0,  1,  2, -1,  0},
        { 0, -1,  1,  2,  1},
        { 1,  0,  0, -1,  2},
        { 2,  1,  0,  0,  1},
        {-1,  2,  1,  0,  0}
    };
    
    GridNavigator robot(terrain, 15, 4, 4);
    robot.find_path(0, 0, 0);
    
    std::cout << "Result: " << robot.final_path_cost << std::endl;
    return 0;
}