Matrix matmul(Matrix a, Matrix b) {
    if (a.cols != b.rows) {
        printf("Matrices cannot be multiplied!");
        exit(1); 
    }
    
    Matrix c = create_matrix(a.rows, b.cols);
    
    for (int i = 0; i < c.rows; i++) {
        for (int j = 0; j < c.cols; j++) {
            float total = 0;
            for (int k = 0; k < a.cols; k++) {
                total += a.values[i][k] * b.values[k][j];
            }
            c.values[i][j] = total;
        }
    }
    
    return c;
}