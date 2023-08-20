import numpy
import numpy as np
import qiskit.quantum_info as qi
from scipy.linalg import expm
from utilities import Utilities
from quantumGate import QuantumGate
from qiskit import QuantumRegister, QuantumCircuit


class CXGate(QuantumGate):
    """
    Represents a CNOT (controlled-X) gate in a quantum system.
    
    The CXGate class provides methods to create a CNOT gate for a specified control and target qubit, compute the 
    amplitude damping channel for the CNOT gate, generate RC (Randomized Compiling) gates for the CNOT gate, and add 
    coherent error to the CNOT gate.
    
    The class inherits from the QuantumGate base class, extending its functionality to specifically handle CNOT gates.
    
    Attributes:
        n_qubits (int): The number of qubits in the quantum system.
        c (int): The control qubit for the CNOT gate.
        t (int): The target qubit for the CNOT gate.
        NUM_RC_CX (int): Number of Randomized Compiling gates.
        LEFT_RC (int): Index for left RC gate.
        RIGHT_RC (int): Index for right RC gate.
    """
    NUM_RC_CX = 16
    LEFT_RC = 0
    RIGHT_RC = 1

    def __init__(self, n_qubits, control, target):
        """
        Initializes the CXGate class with a given number of qubits, control qubit, and target qubit.

        Args:
            n_qubits (int): The number of qubits in the quantum system.
            control (int): The control qubit for the CNOT gate.
            target (int): The target qubit for the CNOT gate.
        """
        super().__init__(n_qubits)
        self.c = control
        self.t = target

    def get_matrix(self):
        """
        Creates and returns the matrix representation of a CNOT gate for the specified control and target qubits.

        Returns:
            numpy.ndarray: The matrix representation of the CNOT gate.
        """
        qc = QuantumCircuit(QuantumRegister(self.n))

        # Dictionary to store (c, t) to (cc, tt) mappings for different values of n
        transformations = {
            3: {(1, 0): (2, 1), (2, 1): (1, 0)},
            4: {(1, 0): (3, 2), (2, 0): (3, 1), (3, 1): (2, 0), (3, 2): (1, 0)}
        }

        # Get the transformed (cc, tt) pair if present, otherwise use the original (c, t)
        cc, tt = transformations.get(self.n, {}).get((self.c, self.t), (self.c, self.t))

        qc.cx(tt, cc)
        return qi.Operator(qc).data.real

    def apply_channel_in_ls(self, error_channel):
        """
        Applies a given error channel to the Liouville matrix representation of the CNOT gate.

        Args:
            error_channel (numpy.ndarray): The error channel to be applied.

        Returns:
            numpy.ndarray: The modified Liouville matrix representation after applying the error channel.
        """
        return np.dot(self.adc_channel(error_channel), self.get_liouville_matrix())

    def adc_channel(self, p):
        """
        Computes the Amplitude Damping Channel (ADC) for the CNOT gate.

        Args:
            p (float): The probability parameter for the amplitude damping channel.

        Returns:
            numpy.ndarray: The ADC matrix for the CNOT gate.
        """
        k0 = [[1, 0], [0, np.sqrt(1 - p)]]
        k1 = [[0, np.sqrt(p)], [0, 0]]

        k0_1 = Utilities().create_kron_product(k0, k0, self.t, self.n)
        k1_1 = Utilities().create_kron_product(k1, k1, self.t, self.n)

        k0_2 = Utilities().create_kron_product(k0, k0, self.c, self.n)
        k1_2 = Utilities().create_kron_product(k1, k1, self.c, self.n)

        channel1 = np.kron(k0_1, np.conj(k0_1)) + np.kron(k1_1, np.conj(k1_1))
        channel2 = np.kron(k0_2, np.conj(k0_2)) + np.kron(k1_2, np.conj(k1_2))

        return np.dot(channel1, channel2)

    def get_rc_in_circ(self, item):
        """
        Generates the Randomized Compiling (RC) gates for the CNOT gate with specified control and target
        qubits for system of n qubits.

        Args:
            item (int): The index of the RC gate.

        Returns:
            list of numpy.ndarray: The RC gates in matrix form.
        """
        # Initialize lists with identity matrices
        ul_matrices = [Utilities.I for _ in range(self.n)]
        ur_matrices = [Utilities.I for _ in range(self.n)]

        # Check for out of range values and correct if needed
        self.c = min(self.c, self.n - 1)
        self.t = min(self.t, self.n - 1)

        # Replace matrices based on the value of c and t
        ul_matrices[self.c] = Utilities.lr[item][self.LEFT_RC]
        ur_matrices[self.c] = Utilities.rr[item][self.LEFT_RC]

        ul_matrices[self.t] = Utilities.lr[item][self.RIGHT_RC]
        ur_matrices[self.t] = Utilities.rr[item][self.RIGHT_RC]

        # Calculate tensor product
        ul = ul_matrices[0]
        ur = ur_matrices[0]

        for i in range(1, self.n):
            ul = np.kron(ul, ul_matrices[i])
            ur = np.kron(ur, ur_matrices[i])

        return [ul, ur]

    def dress_by_rc_gate(self, obj):
        """
        Dresses up the CNOT gate with Randomized Compiling (RC) gates.

        Args:
            obj (numpy.ndarray): The object to be dressed by the RC gates.

        Returns:
            numpy.ndarray: The dressed CNOT gate in matrix form.
        """        dressed_cx = np.dot(IDGate(self.n).get_liouville_matrix(), 0)

        for i in range(self.NUM_RC_CX):
            get_rc = self.get_rc_in_circ(i)
            dressed_cx = dressed_cx + np.dot(np.dot(Utilities().make_liouville(get_rc[self.LEFT_RC]), obj),
                                             Utilities().make_liouville(get_rc[self.RIGHT_RC]))

        return np.dot(dressed_cx, 1 / self.NUM_RC_CX)

    def add_coherent_error(self, is_backword, A, B, obj):
        """
        Adds both controlled and uncontrolled coherent errors to a CNOT gate.

        Args:
            is_backword (bool): Indicates if the gate is applied in a backward direction.
            A (float): Coefficient for the controlled coherent error.
            B (float): Coefficient for the uncontrolled coherent error.
            obj (numpy.ndarray): The object to which the coherent error is added.

        Returns:
            numpy.ndarray: The modified CNOT gate with added coherent errors.
        """
        cont = self.rotate_cont_coh_error[0] if self.c == 0 else (self.rotate_cont_coh_error[1] if self.t == 0 else I)
        uncont = self.rotate_uncont_coh_error[0] if self.c == 0 else (self.rotate_uncont_coh_error[1] if self.t == 0 else I)

        for i in range(1, self.n):
            if i == self.t:
                cont = np.kron(cont, self.rotate_cont_coh_error[1])
                uncont = np.kron(uncont, self.rotate_uncont_coh_error[1])
            elif i == self.c:
                cont = np.kron(cont, self.rotate_cont_coh_error[0])
                uncont = np.kron(uncont, self.rotate_uncont_coh_error[0])
            else:
                cont = np.kron(cont, I)
                uncont = np.kron(uncont, I)

        cx_err = Utilities.make_liouville(expm((-1j if is_backword else 1j) * A * cont - 1j * B * uncont))
        if is_backword:
            return np.dot(cx_err, obj)
        else:
            return np.dot(obj, cx_err)
