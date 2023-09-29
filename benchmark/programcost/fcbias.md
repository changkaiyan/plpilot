Matrix fc(Matrix input, Matrix weights, Matrix bias) {
    // Check dimensions
    if (input.cols != weights.rows) {
        printf("Input and weight dimensions do not match!");
        exit(1); 
    }
    if (bias.rows != weights.cols || bias.cols != 1) {
        printf("Bias dimensions do not match!");
        exit(1);
    }
    
    Matrix result = create_matrix(input.rows, weights.cols);
    
    for (int i = 0; i < result.rows; i++) {
        for (int j = 0; j < result.cols; j++) {
            double total = 0;
            for (int k = 0; k < input.cols; k++) { 
                total += input.values[i][k] * weights.values[k][j];    
            }
            result.values[i][j] = total + bias.values[j][0]; 
        }
    }
    
    return result;
}