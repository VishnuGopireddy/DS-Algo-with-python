#RBR interview prp
#Finding largest square sub-matrix in a given binary matrix
'''
1 1 1 1
0 0 1 1
1 1 1 1  ====> max possible sub-square matrix with all 1's = 2
1 1 1 1

Approach 1 : (Brute Force) => O(N^4)
1. Find all sub-square matrix O(n^3)
2. Check weather a sub0matrix contain all 1's

Approach 2 : Dynamic Programing +> O(n ^ 2)

'''
def display_mat(mat,size):
    '''
    Display the given matrix
    :param mat: multi dimensional array matrix
    :param size: tuple with size
    :return: None
    '''
    # display mat
    for i in range(size[0]):
        for j in range(size[1]):
            print(mat[i][j], end=' ')
        print(' ')


def largest_sub_matrix(mat, size):
    '''
    Finding largest square sub-matrix in a given binary matrix
    :param mat: Binary matrix
    :param size: tuple, size of matrix
    :return: size of largest square sub-matrix in a given binary matrix
    '''
    sol = [[0 for i in range(size[1])] for j in range(size[0])]
    # display mat
    display_mat(mat, size)
    print('----------------')
    for i in range(size[0]):
        for j in range(size[1]):
            if i == 0 or j == 0:
                sol[i][j] = mat[i][j]
    for i in range(1, size[0]):
        for j in range(1, size[1]):
            if mat[i][j] == 1:
                sol[i][j] = min(sol[i-1][j-1], sol[i][j-1], sol[i-1][j]) + 1
            else:
                sol[i][j] = 0

    display_mat(sol,size)

size = (5,4)
mat = [[1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

largest_sub_matrix(mat, size)