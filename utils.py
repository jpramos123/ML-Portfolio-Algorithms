# Implementar a inversão de matriz 2x2 e 3x3 - OK
# Implementar metodo para multiplicação de matriz - OK


def matmul(mat1, mat2):
    """
        This function make a matrix multiplication
        or return an feedback if the multiplication
        isn't valid.
    """

    if len(mat1[0]) == len(mat2):

        n = len(mat1)
        p = len(mat2[0])
        m = len(mat1[0])
        
        mat3 = [[0 for i in range(p)] for j in range(n)]
        
        for i in range(n):
            for j in range(p):
                sum = 0
                for k in range(m):
                    sum = sum + mat1[i][k] * mat2[k][j]
                mat3[i][j] = sum
        return mat3

    else:
        print("Invalid multiplication")
        return -1

def find_determinant(mat):

    if len(mat) == 2:
        return (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
    elif len(mat) == 3:
        
        return ((mat[0][0]*mat[1][1]*mat[2][2]) 
              + (mat[0][1]*mat[1][2]*mat[2][0]) 
              + (mat[0][2]*mat[1][0]*mat[2][1]) 
              - (mat[0][2]*mat[1][1]*mat[2][0])
              - (mat[0][1]*mat[1][0]*mat[2][2])
              - (mat[0][0]*mat[1][2]*mat[2][1])
             )
    else:
        print("Not possible to calculate")
        return -1          
    
def transpose(mat):
    
    n_row = len(mat)
    n_col = len(mat[0])

    new_mat = [[0 for i in range(n_row)] for j in range(n_col)]

    for i in range(n_row):
        for j in range(n_col):
            new_mat[j][i] = mat[i][j]

    return new_mat


def invert_mat(mat):

    """
        This function invert a 2x2 or 3x3 matrix
        if high scaled matrix is passed it will return
        a feedback message
    """        

    if len(mat) == len(mat[0]):

        if len(mat) == 2:
            new_mat = [[0 for i in range(2)] for j in range(2)]
            determinant = find_determinant(mat)

            new_mat[0][0] = mat[1][1]
            new_mat[1][1] = mat[0][0] 
            new_mat[0][1] = (-mat[0][1])
            new_mat[1][0] = (-mat[1][0])

            for i in range(2):
                for j in range(2):
                    new_mat[i][j] = (1/determinant) * new_mat[i][j]
            
            return new_mat

        elif len(mat) == 3:
            new_mat = [[0 for i in range(3)] for j in range(3)]
            determinant = find_determinant(mat)

            new_mat[0][0] = +((mat[1][1] * mat[2][2]) - (mat[1][2] * mat[2][1]))
            new_mat[0][1] = -((mat[1][0] * mat[2][2]) - (mat[1][2] * mat[2][0]))
            new_mat[0][2] = +((mat[1][0] * mat[2][1]) - (mat[1][1] * mat[2][0]))
            new_mat[1][0] = -((mat[0][1] * mat[2][2]) - (mat[0][2] * mat[2][1]))
            new_mat[1][1] = +((mat[0][0] * mat[2][2]) - (mat[0][2] * mat[2][0]))
            new_mat[1][2] = -((mat[0][0] * mat[2][1]) - (mat[0][1] * mat[2][0]))
            new_mat[2][0] = +((mat[0][1] * mat[1][2]) - (mat[0][2] * mat[1][1]))
            new_mat[2][1] = -((mat[0][0] * mat[1][2]) - (mat[0][2] * mat[1][0]))
            new_mat[2][2] = +((mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0]))

            for i in range(3):
                for j in range(3):
                    new_mat[i][j] = (1/determinant) * new_mat[i][j]
            return transpose(new_mat)
        

        else:
            print("Not possible to invert")
            return -1
    else:
        print("Not possible to invert")
        return -1            

def multiply_arr(arr, betha):
    new_arr = [v for v in arr]
    for i in range(len(arr)):
        new_arr[i] = float(new_arr[i]*betha)
    return new_arr

def sum_arr(arr, val_to_sum):
    new_arr = [v for v in arr]
    for i in range(len(arr)):
        new_arr[i] = float(new_arr[i] + val_to_sum)
    return new_arr

def buildData(data_frame):

    x = [[1] for i in range(data_frame.shape[0])]
    y = [[] for i in range(data_frame.shape[0])]
    for i in range(data_frame.shape[1]):
        for j in range(data_frame.shape[0]):
            if i < (data_frame.shape[1] - 1):
                # Getting features
                x[j].append(data_frame.iloc[j,i])
            else:
                y[j].append(data_frame.iloc[j,i])
    return [x,y]

def findBeta(features, target):

    xt_x = matmul(transpose(features),features)
    xt_y = matmul(transpose(features),target)
    beta = matmul(invert_mat(xt_x),xt_y)
    return beta

def linear(dataset):

    beta = findBeta(dataset[0], dataset[1])
    print("Beta Gerado: ", beta)
    n = len(beta)
    x = [i for i in range(3000)]
    y = [0 for i in range(len(x))]

    
    for j in range(len(x)):
        for i in range(n-1):
            y[j] = y[j] + x[j]*beta[i+1][0]
        y[j] = y[j] + beta[0][0]
    
    return [x,y]

def quadratic(dataset):
    
    
    for v in dataset[0]:
        v.append(v[1]*v[1])

    beta = findBeta(dataset[0], dataset[1])

    print("Beta Gerado: ", beta)

    n = len(beta)
    x = [i for i in range(3000)]
    y = [0 for i in range(len(x))]

    for j in range(len(x)):
        y[j] = y[j] + x[j]*beta[1][0] + x[j]*x[j]*beta[2][0] + beta[0][0]

    return [x,y]

def buildPoints(data_frame):

    x = [[] for i in range(data_frame.shape[0])]
    y = [[] for i in range(data_frame.shape[0])]
    for i in range(data_frame.shape[1]):
        for j in range(data_frame.shape[0]):
            if i < (data_frame.shape[1] - 1):
                # Getting features
                x[j].append(data_frame.iloc[j,i])
            else:
                y[j].append(data_frame.iloc[j,i])
    return [x,y]



if __name__ == "__main__":
    
    mat1 = [[5,6,1],
            [3,7,1]]
            
    mat2 = [[1,2],[3,4]]


    print(transpose(mat1))