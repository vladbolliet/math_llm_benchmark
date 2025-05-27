# filename: codebase/solve_linear_system.py
import numpy as np
import os

def compute_nullspace(C, rtol=1e-10):
    """
    Compute an orthonormal basis for the nullspace of matrix C.
    Parameters
    ----------
    C : ndarray, shape (m, n)
        Input matrix.
    rtol : float
        Relative tolerance for small singular values.
    Returns
    -------
    N : ndarray, shape (n, k)
        Orthonormal basis for the nullspace of C.
    """
    u, s, vh = np.linalg.svd(C, full_matrices=True)
    rank = (s > rtol * s[0]).sum()
    null_space = vh[rank:].T
    return null_space

def main():
    # Define matrices and vectors
    # A: shape (2,3), b: shape (2,), C: shape (2,3)
    A = np.array([[1, 2, -1],
                  [3, 0, 4]], dtype=float)
    b = np.array([2, 7], dtype=float)
    C = np.array([[1, -1, 0],
                  [0, 1, -1]], dtype=float)

    # Step 1: Compute nullspace of C
    N = compute_nullspace(C)
    # N: shape (3, k), k = dimension of nullspace

    # Step 2: Express x = N y, substitute into A x = b
    AN = np.dot(A, N)  # shape (2, k)

    # Step 3: Solve AN y = b for y
    # If AN is square, use solve; else, use least squares
    if AN.shape[0] == AN.shape[1]:
        y = np.linalg.solve(AN, b)
    else:
        y, residuals, rank, s = np.linalg.lstsq(AN, b, rcond=None)
    # Step 4: Recover x
    x = np.dot(N, y)

    # Step 5: Save and print results
    # Save x to data/solution_x.npy
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    np.save(os.path.join(output_dir, "solution_x.npy"), x)

    # Print results
    np.set_printoptions(precision=10, suppress=True)
    print("Solution x (A x = b, C x = 0):")
    print(x)
    print("\nVerification:")
    print("A x = " + str(np.dot(A, x)) + " (should be b = " + str(b) + ")")
    print("C x = " + str(np.dot(C, x)) + " (should be 0)")
    print("\nSolution saved to data/solution_x.npy")

if __name__ == "__main__":
    main()
