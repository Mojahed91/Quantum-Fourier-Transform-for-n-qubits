import numpy as np


class Utilities:
    """
    Contains static methods for performing operations on quantum gates, such as making liouville operators, computing tensor (Kronecker) products, and creating single qubit gates in an n-qubit system.

    Constants:
        X, Y, Z, I : Pauli matrices.
        H : Hadamard matrix.
        I4 : 4x4 Identity matrix.
        lr, rr : Sets of 2-qubit operators for left and right operators.
        cnot1 : CNOT matrix with control qubit 1.
        pauli : List of Pauli matrices.
    """
    # Constants and Globals
    X, Y, Z, I = [np.array([[0, 1], [1, 0]]),
                  np.array([[0, -1j], [1j, 0]]),
                  np.array([[1, 0], [0, -1]]),
                  np.eye(2)]
    H = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
    I4 = np.kron(I, I)
    lr = [[I, I], [I, X], [I, Y], [I, Z], [Y, I], [Y, X], [Y, Y], [Y, Z], [X, I], [X, X], [X, Y], [X, Z], [Z, I],
          [Z, X], [Z, Y], [Z, Z]]
    rr = [[I, I], [I, X], [Z, Y], [Z, Z], [Y, X], [Y, I], [X, Z], [X, Y], [X, X], [X, I], [Y, Z], [Y, Y], [Z, I],
          [Z, X], [I, Y], [I, Z]]
    cnot1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

    pauli = [X, Y, Z, I]

    @staticmethod
    def make_liouville(oper):
        """
        Compute the Liouville representation of a given operator.

        Args:
            oper (np.array): The operator to be converted.

        Returns:
            np.array: The Liouville representation of the operator.
        """
        return np.kron(oper, np.conj(oper))

    @staticmethod
    def recursive_kron(matrices):
        """
        Compute the Kronecker product of a list of matrices recursively.

        Args:
            matrices (list): List of matrices.

        Returns:
            np.array: The Kronecker product of the matrices.
        """
        if len(matrices) == 1:
            return matrices[0]
        return np.kron(matrices[0], Utilities.recursive_kron(matrices[1:]))

    @staticmethod
    def create_kron_product(matrix1, matrix2, position, n):
        """
        Compute the tensor product of two matrices with respect to a position in an n-qubit system.

        Args:
            matrix1 (np.array): First matrix.
            matrix2 (np.array): Second matrix.
            position (int): Position in the n-qubit system.
            n (int): Total number of qubits.

        Returns:
            np.array: The tensor product of the matrices with respect to the position.
        """
        product = matrix1 if position == 0 else Utilities.I
        for i in range(1, n):
            next_matrix = matrix2 if position == i else Utilities.I
            product = np.kron(product, next_matrix)
        return product

    @staticmethod
    def single_q_gate_for_n_q(t, n, oper):
        """
        Return a single qubit gate for an n-qubit system.

        Args:
            t (int): Target qubit.
            n (int): Total number of qubits.
            oper (np.array): The single qubit gate.

        Returns:
            np.array: The single qubit gate for the n-qubit system.
        """
        # Create a list of identity matrices
        matrices = [Utilities.I] * n

        # Replace the t-th matrix with the operator
        matrices[t] = oper

        # Compute the Kronecker product
        result = matrices[0]
        for mat in matrices[1:]:
            result = np.kron(result, mat)

        return result

    def single_q_gate_for_n_q_in_ls(t, n, oper):
                """
        Return a single qubit gate for an n-qubit system in Liouville space.

        Args:
            t (int): Target qubit.
            n (int): Total number of qubits.
            oper (np.array): The single qubit gate.

        Returns:
            np.array: The single qubit gate for the n-qubit system in Liouville space.
        """
        return Utilities.make_liouville(Utilities.single_q_gate_for_n_q(t, n, oper))

