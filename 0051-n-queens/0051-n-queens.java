class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        int[] queens = new int[n]; // queens[row] = column index of queen in that row

        boolean[] usedCols = new boolean[n];
        boolean[] usedDiag1 = new boolean[2 * n]; // row - col + n (normalized)
        boolean[] usedDiag2 = new boolean[2 * n]; // row + col

        backtrack(0, n, queens, usedCols, usedDiag1, usedDiag2, result);
        return result;
    }

    private void backtrack(int row, int n, int[] queens, boolean[] usedCols,
                            boolean[] usedDiag1, boolean[] usedDiag2,
                            List<List<String>> result) {
        if (row == n) {
            result.add(buildBoard(queens, n));
            return;
        }

        for (int col = 0; col < n; col++) {
            int d1 = row - col + n;
            int d2 = row + col;

            if (usedCols[col] || usedDiag1[d1] || usedDiag2[d2]) {
                continue; // conflict — skip this column
            }

            // place queen
            queens[row] = col;
            usedCols[col] = true;
            usedDiag1[d1] = true;
            usedDiag2[d2] = true;

            backtrack(row + 1, n, queens, usedCols, usedDiag1, usedDiag2, result);

            // remove queen (backtrack)
            usedCols[col] = false;
            usedDiag1[d1] = false;
            usedDiag2[d2] = false;
        }
    }

    private List<String> buildBoard(int[] queens, int n) {
        List<String> board = new ArrayList<>();
        for (int row = 0; row < n; row++) {
            char[] rowChars = new char[n];
            Arrays.fill(rowChars, '.');
            rowChars[queens[row]] = 'Q';
            board.add(new String(rowChars));
        }
        return board;
    }
}