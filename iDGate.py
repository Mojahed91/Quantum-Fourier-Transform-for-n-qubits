import numpy as np
from quantumGate import QuantumGate
from utilities import Utilities


class IDGate(QuantumGate):
    def __init__(self, n_qubits):
        super().__init__(n_qubits)

    def get_matrix(self):
        return Utilities.single_q_gate_for_n_q(0, self.n, Utilities.I)

    def run_pauli_combinations(self, oper):
        """Compute the inverse operation in Liouville space for a given number 'n' of qubits."""
        init = Utilities.recursive_kron([Utilities.I] * self.n)
        dressed_oper = np.dot(np.kron(init, init), 0)

        def generate_pauli_combinations(depth, indices):
            nonlocal dressed_oper
            if depth == self.n:
                combined_pauli = Utilities.recursive_kron([Utilities.pauli[i] for i in indices])
                sig_b_L = Utilities.make_liouville(combined_pauli)
                dressed_oper = dressed_oper + np.dot(np.dot(sig_b_L, oper), sig_b_L)
                return
            for i in range(4):
                generate_pauli_combinations(depth + 1, indices + [i])

        generate_pauli_combinations(0, [])
        return np.dot(dressed_oper, 1 / (4 ** self.n))

    def dress_id_operator_by_rc_gates(self, oper, n):
        """Dress up the Identity gate with Randomised Compiling gates."""
        return self.run_pauli_combinations(oper, n)
