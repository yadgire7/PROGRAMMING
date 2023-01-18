# Problem Statement: Given a matrix if an element in the matrix is 0 
# then you will have to set its entire column and row to 0 and then return the matrix.

# Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output: [[1,0,1],[0,0,0],[1,0,1]]

#######################
# brute force approach#
#######################

def bruteSolution(mat):
    row,col=0,0
#  consider that all the elements of the matrix are non-negative integers
#  so convert the elements in the row and column containing 0 to -1(any negative interger)
# such that while traversing, the consistency of the matrix (0s) is retained
    for i in range(len(mat)):
        for j in range(len(mat[0])):       
            if mat[i][j]==0:
                row, col = i,j
                for c in range(len(mat[0])):
                    mat[row][c]=-1
                for r in range(len(mat)):
                    mat[r][col]=-1
# changing negative numbers to 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==-1:
                mat[i][j]=0

    return mat


if __name__ == "__main__":
    a = solution([[1,1,1],[1,0,1],[1,1,1]])
    print(a)