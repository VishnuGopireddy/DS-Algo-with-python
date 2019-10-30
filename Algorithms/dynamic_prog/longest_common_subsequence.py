#RBR Interview prep
#Longest Common sub-sequence
'''
Approach: Dynamic Program O(n^2)

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

def longest_common_sub_seq(str1, str2):
    '''
    Computes longest common subsequence of str1 and str2
    :param str1: string1
    :param str2:  string2
    :return: Inetger
    '''
    len1, len2 = len(str1), len(str2)
    sol = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if i == 0 or j == 0:
                sol[i][j] = 0
            else:
                if str1[j - 1] == str2[i - 1]:
                    sol[i][j] = sol[i-1][j-1] + 1
                else:
                    sol[i][j] = max(sol[i-1][j], sol[i][j-1])


    #display_mat(sol, (len2+1, len1+1))
    return sol[-1][-1]

str1 = 'gxtxayb'
str2 = 'aggtab'
print('Lognest common subsequence of %s and %s is %d:' %(str1, str2, longest_common_sub_seq(str1, str2)))