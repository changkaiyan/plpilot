Matrix matmul(Matrix a, Matrix b) {
    if (a.cols != b.rows) {
        printf("Matrices cannot be multiplied!");
        exit(1); 
    }
    
    Matrix c = create_matrix(a.rows, b.cols);
    
    for (int i = 0; i < c.rows; i++) {
        for (int j = 0; j < c.cols; j++) {
            float total = 0;
            vector_mul(a,b,i,j,total);
            c.values[i][j] = total;
        }
    }
    
    return c;
}