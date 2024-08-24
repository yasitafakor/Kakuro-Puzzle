## Kakuro Puzzle Solver Project

### Overview

This project develops a solver for the Kakuro puzzle using two primary approaches: backtracking and Constraint Satisfaction Problems (CSP). The goal is to efficiently solve Kakuro puzzles, which are logic-based puzzles similar to crosswords but with numbers.

### Components

1. **Backtracking Solver (`Kakuro` class)**:
   - **Initialization**: Sets up a 5x5 Kakuro board with constraints for each constraint cell.
   - **Validation**: Checks if the current board configuration meets the constraints.
   - **Solver**: Uses a backtracking algorithm to fill in numbers, ensuring they meet both row and column constraints. The method is straightforward but can be slow for larger puzzles.

2. **Improved CSP Solver (`Kakuro` class)**:
   - **Initialization**: Similar board setup with constraints and domains for each constraint cell.
   - **Forward Checking**: Enhances the backtracking approach by dynamically pruning the search space. It updates possible values (domains) for constraint cells as the board is filled.
   - **Solver**: Solves the puzzle by recursively filling cells while respecting constraints both vertically and horizontally. Forward Checking helps in reducing computation time compared to pure backtracking.

### Usage

- **Backtracking**: Use the `solve_kakuro_backtrack` method to solve the puzzle using a simple backtracking approach.
- **CSP**: Use the `solve` method to solve the puzzle more efficiently with Forward Checking.
