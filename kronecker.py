from math import sqrt

global Z
Z = 32

def kron_product(m1, m2):
    """
    Compute the kronecker product of two squared matrices
    """
    if len(m1[0]) != len(m2):
        raise ValueError("m1 and m2 must be matrices of same dimensions")
    # initialize the result matrix
    n = len(m1)
    n_squared = len(m1)**2
    result = [[0 for _ in range(n_squared)] for _ in range(n_squared)]
    # compute the kronecker product
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    result[i*n+j][k*n+l] = m1[i][k] * m2[j][l]
    return result

def kron_product_aware(A, B):
    n = len(m1)
    n_squared = len(m1)**2
    C = [[0 for _ in range(n_squared)] for _ in range(n_squared)]
    # choix de blocking optimal
    alpha = int(sqrt(Z/3))
    print(alpha)
    for I in range(0, n, alpha):
        imax = min(I+alpha, n)
        for J in range(0, n, alpha):
            jmax = min(J+alpha, n)
            for K in range(0, n, alpha):
                kmax = min(K+alpha, n)
                for L in range(0, n, alpha):
                    lmax = min(L+alpha, n)
                    for i in range(I, imax):
                        for j in range(J, jmax):
                            for k in range(K, kmax):
                                for l in range(L, lmax):
                                        C[i*n+j][k*n+l] = A[i][k] * B[j][l]
    return C

def kron_product_oblivious(A, B, n):
    C = [[0 for _ in range(n**2)] for _ in range(n**2)]
    # choix de blocking optimal
    alpha = int(sqrt(Z/3))
    print(alpha)
    if (n<=alpha):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        C[i*n+j][k*n+l] = A[i][k] * B[j][l]
    
    moitie = int(n/2)
    # découpe récursive des matrices A et B
    return C

if __name__ == '__main__':
    m1 = [[1, 2], [3, 1]]
    m2 = [[0, 3], [2, 1]]
    print(kron_product(m1,m2))

    print(kron_product_aware(m1,m2))