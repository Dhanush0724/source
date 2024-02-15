public class QueenBT {
    final int n = 4;

    void printSolution(int board[][]) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                System.out.print(board[i][j] + " ");
            System.out.println();
        }
    }

    boolean isSafe(int board[][], int row, int col) {
        int i, j;

        // Check the row on the left side
        for (i = 0; i < col; i++)
            if (board[row][i] == 1)
                return false;

        // Check upper diagonal on the left side
        for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 1)
                return false;

        // Check lower diagonal on the left side
        for (i = row, j = col; i < n && j >= 0; i++, j--)
            if (board[i][j] == 1)
                return false;

        return true;
    }

    boolean solveNQUtil(int board[][], int col) {
        if (col >= n)
            return true;

        for (int i = 0; i < n; i++) {
            if (isSafe(board, i, col)) {
                board[i][col] = 1;

                if (solveNQUtil(board, col + 1))
                    return true;

                board[i][col] = 0; // Backtrack
            }
        }

        return false;
    }

    boolean solveNQ() {
        int board[][] = new int[n][n];

        if (!solveNQUtil(board, 0)) {
            System.out.println("Solution does not exist");
            return false;
        }

        printSolution(board);
        return true;
    }

    public static void main(String[] args) {
        QueenBT queen = new QueenBT();
        queen.solveNQ();
    }
}
