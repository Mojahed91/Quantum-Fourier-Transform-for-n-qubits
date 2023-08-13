from utilities import Utilities


class QuantumGate:
    def __init__(self, n_qubits):
        self.n = n_qubits
        self.rotate_cont_coh_error = [0] * n_qubits
        self.rotate_uncont_coh_error = [0] * n_qubits

    def get_matrix(self):
        raise NotImplementedError

    def apply_channel_in_ls(self, error_channel):
        return

    def get_liouville_matrix(self):
        return Utilities.make_liouville(self.get_matrix())

    def set_rotation_as_coherent_error(self, rotate_cont_coh_error, rotate_uncont_coh_error):
        for qubit in range(self.n):
            self.rotate_cont_coh_error[qubit] = rotate_cont_coh_error[qubit]
            self.rotate_uncont_coh_error[qubit] = rotate_uncont_coh_error[qubit]

