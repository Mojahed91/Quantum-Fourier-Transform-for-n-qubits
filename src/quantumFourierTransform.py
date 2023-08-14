import numpy as np
from quantumCircuitImplementation import QuantumCircuitImplementation
from utilities import Utilities
from cXGate import CXGate
from iDGate import IDGate
from zGate import ZGate


class QuantumFourierTransform(QuantumCircuitImplementation):
    """
    Implements methods for Quantum Fourier Transform (QFT) and its inverse.
    Includes functionalities for error adjustments and amplitude damping.
    """

    # Constants
    CONTROLLABLE_COHERENT_ERROR_CX = 0.015
    UNCONTROLLABLE_COHERENT_ERROR_CX = 0.012
    AVG_ONE_QUBIT_ERROR = 0.00
    AVG_TWO_QUBIT_ERROR = 0.001
    rot_cont_coh_error_cx = [Utilities.X, Utilities.Y]
    rot_uncont_coh_error_cx = [Utilities.X, Utilities.Y]

    def __init__(self, n_qubits):
        super().__init__(n_qubits)
        self.controllable_coh_err = self.CONTROLLABLE_COHERENT_ERROR_CX
        self.uncontrollable_coh_err = self.UNCONTROLLABLE_COHERENT_ERROR_CX
        self.avg_one_qubit_error = self.AVG_ONE_QUBIT_ERROR
        self.avg_two_qubit_error = self.AVG_TWO_QUBIT_ERROR

    # Setters and getters for coherent errors
    @property
    def controllable_coh_err_cx(self):
        return self.controllable_coh_err

    @controllable_coh_err_cx.setter
    def controllable_coh_err_cx(self, cont):
        self.controllable_coh_err = cont

    @property
    def uncontrollable_coh_err_cx(self):
        return self.uncontrollable_coh_err

    @uncontrollable_coh_err_cx.setter
    def uncontrollable_coh_err_cx(self, un_cont):
        self.uncontrollable_coh_err = un_cont

    def apply_gates(self, t, c, rn, is_inverse, is_add_rc):
        """
            Return the operator in Liouville space with z-rotation, cx with error,
            and ADC followed by further z-rotations.
        """
        z_rot_bef = ZGate(self.n_qubits, rn, +1, t).get_liouville_matrix()
        z_inv_rot_bef = ZGate(self.n_qubits, rn, -1, t).get_liouville_matrix()
        cx_obj = CXGate(self.n_qubits, c, t)
        cx_obj.set_rotation_as_coherent_error(self.rot_cont_coh_error_cx, self.rot_uncont_coh_error_cx)
        cx_adc = cx_obj.apply_channel_in_ls(self.avg_two_qubit_error)
        cx_err = cx_obj.add_coherent_error(is_inverse, self.controllable_coh_err, self.uncontrollable_coh_err, cx_adc)

        if is_add_rc:
            cx_err = cx_obj.dress_by_rc_gate(cx_err)

        z_inv_rot_aft = ZGate(self.n_qubits, rn, -1, c).get_liouville_matrix()
        z_rot_aft = ZGate(self.n_qubits, rn, +1, c).get_liouville_matrix()

        if is_inverse:
            return np.dot(np.dot(np.dot(np.dot(z_inv_rot_bef, cx_err), z_rot_aft), cx_err), z_inv_rot_aft)
        return np.dot(np.dot(np.dot(np.dot(z_rot_aft, cx_err), z_inv_rot_aft), cx_err), z_rot_bef)

    def build_inverse_qft_block(self, last_q, target_q, is_add_rc):
        """
        Constructs a block for the inverse Quantum Fourier Transform.
        """
        qft_i = IDGate(self.n_qubits).get_liouville_matrix()
        for i in range(last_q - target_q):
            control = last_q - i
            rn = np.pi / pow(2, (self.n_qubits - target_q - i))
            qft_i = np.dot(self.apply_gates(target_q, control, rn, True, is_add_rc), qft_i)
        return qft_i

    def build_qft_block(self, last_q, target_q, is_add_rc):
        """
        Constructs a block for the Quantum Fourier Transform.
        """
        qft = IDGate(self.n_qubits).get_liouville_matrix()
        for i in range(last_q - target_q):
            control = target_q + 1 + i
            rn = np.pi / pow(2, (2 + i))
            qft = np.dot(self.apply_gates(target_q, control, rn, False, is_add_rc), qft)
        return qft

    def compute_qft(self, is_add_rc):
        """
        Compute the Quantum Fourier Transform.
        """
        qft = IDGate(self.n_qubits).get_liouville_matrix()
        for i in range(self.n_qubits):
            bloc = self.build_qft_block(self.n_qubits - 1, i, is_add_rc)
            qft = np.dot(bloc, qft)
            uH = Utilities.single_q_gate_for_n_q_in_ls(i, self.n_qubits, Utilities.H)
            qft = np.dot(uH, qft)
        return qft

    def compute_inverse_qft(self, is_add_randomised_compiling):
        """
        Compute the inverse Quantum Fourier Transform.
        """
        qft_i = IDGate(self.n_qubits).get_liouville_matrix()
        i = self.n_qubits - 1
        while i >= 0:
            uH = Utilities.single_q_gate_for_n_q_in_ls(i, self.n_qubits, Utilities.H)
            qft_i = np.dot(uH, qft_i)
            bloc = self.build_inverse_qft_block(self.n_qubits - 1, i, is_add_randomised_compiling)
            qft_i = np.dot(bloc, qft_i)
            i = i - 1
        return qft_i

    def forward_circuit(self):
        return self.compute_qft(False)

    def backward_circuit(self):
        return self.compute_inverse_qft(False)

    def forward_circuit_with_rc(self):
        return self.compute_qft(True)

    def backward_circuit_with_rc(self):
        return self.compute_inverse_qft(True)


