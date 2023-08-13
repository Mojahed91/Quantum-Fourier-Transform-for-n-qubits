import numpy as np
from quantumGate import QuantumGate
from utilities import Utilities


class ZGate(QuantumGate):
    def __init__(self, n_qubits, theta, sign_rot, target):
        super().__init__(n_qubits)
        self.theta = theta
        self.sign_rot = sign_rot
        self.target = target

    def get_matrix(self):
        """Return Z-rotation matrix for given angle theta."""
        zr = [[np.exp(-1j * self.sign_rot * (self.theta / 2)), 0], [0, np.exp(1j * self.sign_rot * (self.theta / 2))]]
        return Utilities.single_q_gate_for_n_q(self.target, self.n, zr)

