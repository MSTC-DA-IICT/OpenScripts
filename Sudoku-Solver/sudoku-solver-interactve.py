######## run this script in terminal to solve a sudoku problem

# function that takes a 9*9 matrix and returns the solution
def solveSudoku(matrix):
    
    # function: checks whether the assumed value can inserted into the cell
    def isValid(matrix, i, j, val):
    
        # checking same value in the column
        for x in range(9):
            if matrix[x][j] == val:
                return False
        # checking same value in the row
        for y in range(9):
            if matrix[i][y] == val:
                return False
        # checking value in 3*3 matrix
        start_i = i//3 * 3
        start_j = j//3 * 3
        for x in range(start_i, start_i+3, 1):
            for y in range(start_j, start_j+3, 1):
                if matrix[x][y] == val:
                    return False
        # If not returned false yet, means assumed value is correct
        return True
    
    # function: checks & filles every cell
    def fillCellValue(matrix, i, j):

        # When reaches (8,9) we end the program
        if(i==len(matrix)-1 and j == len(matrix)):
            return True

        # E.g (x, 9) => (x+1, 0) || when reaches column 9 we increase the row by one
        if(j==len(matrix)):
            i = i + 1
            j = 0
    
        # If the value in cell is not zero => move to next cell
        if(matrix[i][j] != 0):
            return fillCellValue(matrix, i, j+1)
    
        # If matrix[x][y] = 0, find a valid value to fill in the cell
        for val in range(1, 10, 1):
            if isValid(matrix, i, j, val):
                matrix[i][j] = val
                # checking for next cell
                if fillCellValue(matrix, i, j+1):
                    return True
            # when assumption is proved wrong
            matrix[i][j] = 0
        
        # No solution of the problem exist
        return False
    
    # return statement of the solveSudoku function
    if fillCellValue(matrix, 0, 0):
        return matrix
    else:
        return "No solution exists"

# function to print the sudoku matrix 
def printSudoku(matrix):
    for i in range(9):
        for j in range(9):
            print(matrix[i][j], end = " ")
        print()

# main function   
if __name__ == "__main__":
    
    print("Hello, let's solve 9*9 sudoku, but you have provide me the values: ")
    
    row = 9
    col = 9
    
    matrix = []
    print("Enter values rowwise")
    
    # taking input from user
    for i in range(row):
        arow = list(map(int, input("Elements of "+str(i)+" row are: ").strip().split(' ')[:col]))
        matrix.append(arow)
    
    # printing the answer for the user
    if (solveSudoku(matrix) != "No solution exists"):
        print("Here's is the solved sudoku")
        printSudoku(solveSudoku(matrix))
    else:
        print(solveSudoku(matrix))
    
    


    
    
    