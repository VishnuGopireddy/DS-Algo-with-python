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


def largest_sub_matrix(mat, size):
    '''
    Finding largest square sub-matrix in a given binary matrix
    :param mat: Binary matrix
    :param size: tuple, size of matrix
    :return: size of largest square sub-matrix in a given binary matrix
    '''
    sol = [[0 for i in range(size[1])] for j in range(size[0])]
    for i in range(size[0]):
        for j in range(size[1]):
            print(sol[i][j], end=' ')
        print(' ')

size = (5,4)
mat = [[1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

print (mat)
largest_sub_matrix(mat, size)