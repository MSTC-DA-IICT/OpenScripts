## Sudoku Solver

### **Scripts Details**

1. `sudoku-solver-function.py` - This script has a function defined to solve any sudoku. Import this scipt in any project and use the function solveSudoku() giving a 9*9 unsolved sudoku matrix as argument and it will return you the solved matrix or the solution does not exist as an answer.

2. `sudoku-solver-interactive.py` - Run this scipt in the terminal, input as the script asks to and it will print the solved sudoku on the terminal.


### **To run Script on terminal**

1. [Download python IDLE](https://www.python.org/downloads/)
2. Confirm python is installed correctly by typing `python --version`. If python version isn't visible or you encounter any other issue, install python IDLE again.
2. Go to the directory where you have the script and open command prompt.
3. Now, type `python sudoku-solver-interactive.py` to run the script. Input as the script ask to and get your solved sudoku matrix.

### **Functions description**

1. `solveSudoku(matrix)`:<br>
Inputs:  
- matrix: 9*9 unsolved sudoku matrix

This function will take an unsolved sudoku matrix as input and will return either the solved sudoku matrix or "There is no solution to this sudoku matrix".

2. `isValid(matrix, i, j, val)`:<br>
Inputs:  
- matrix: 9*9 sudoku matrix
- i : row number
- j : column number
- val : val that is assumed to be assigned at matrix[i][j]

This function return false if we cannot assgin val to matrix[i][j], else it will return true if we can assign.

3. `fillCellValue(matrix, i, j)`:<br>
Inputs:  
- matrix: 9*9 sudoku matrix
- i : row number
- j : column number

This functions checks and fills the matrix[i][j] cell with proper value.

4. `printSudoku(matrix)`:<br>
Inputs:  
- matrix: 9*9 sudoku matrix

This function just prints the sudoku matrix in a more readable way.
<br>

## Sudoku Problem

The Sudoku Problem is a classic example of backtracking problem. We start filling the cells (whose value is zero) taking one possible value at a time. If at any step we find that the value we assumed is wrong, we go back to the most nearest step where we can assume a different value. We discard the assumption made previous and start with a different assumption this time. 

This process of assuming a value however if proved wrong, track back the path and start with a fresh assumption is known as backtracking. 

### __Points to keep in mind:__
These are the points or parts of the problem I took time to get hold of.

Assumed: Indexing from 0-8 => 9 indexs total
1. Ending the program when reached (8,9) cell. When we filled (8,8) cell, the problem is done however we only know we have completed the traversal only with condition if(row==8 and col == 9).

2. The fact that we have to fill 8 columns, in order to go the next row we apply condition if(column == 9), then move to next row and start from column 0.
