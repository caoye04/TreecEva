import java.util.*;

public class ComplexComputation {
    public static int recursiveSum(int n) {
        if (n <= 1) return n;
        return n + recursiveSum(n - 1);
    }
    
    public static int bitwiseTransform(int x, int y) {
        return (x << 2) ^ (y >> 1) & 0xF;
    }
    
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        List<String> tokens = Arrays.asList("15", "22", "8", "33");
        Map<String, Integer> mapping = new HashMap<>();
        mapping.put("alpha", 5);
        mapping.put("beta", 12);
        mapping.put("gamma", 7);
        
        int accumulator = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                accumulator += matrix[i][j] * (i + 1) * (j + 1);
            }
        }
        
        int transformResult = 0;
        for (String token : tokens) {
            int value = Integer.parseInt(token);
            transformResult ^= bitwiseTransform(value, accumulator % 16);
        }
        
        int recursiveComponent = recursiveSum(mapping.get("beta"));
        String hexString = "AF";
        int hexValue = Integer.parseInt(hexString, 16);
        
        double powerComponent = Math.pow(mapping.get("alpha"), 3);
        int finalAdjustment = (int)(powerComponent + Math.sqrt(hexValue));
        
        int result = (transformResult + recursiveComponent + finalAdjustment) % 1000;
    }
}