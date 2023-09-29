Matrix attention(Matrix Q, Matrix K, Matrix V) {
    // Check input shapes
    if (Q.cols != K.rows || K.cols != V.rows) {
        printf("QKV dimensions do not match!");
        exit(1);
    }
    
    // Compute attention weights (unnormalized)
    Matrix A = multiply_matrices(Q, K.T); 
    
    int cols = V.cols;
    Matrix result = create_matrix(Q.rows, cols);
    
    for (int i = 0; i < Q.rows; i++) {
        double scale = 0;
        // Compute sum of A along row for normalization  
        for (int j = 0; j < K.cols; j++) {
            scale += A.values[i][j];         
        }
        
        for (int j = 0; j < cols; j++) {
            double total = 0;
            // Compute weighted sum along V columns
            for (int k = 0; k < K.cols; k++) {
                total += A.values[i][k] / scale * V.values[k][j]; 
            }
            result.values[i][j] = total;
        }
    }
    
    delete_matrix(A);
    return result;
}