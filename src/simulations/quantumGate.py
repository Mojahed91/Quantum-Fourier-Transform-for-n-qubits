from utilities import Utilities


class QuantumGate:
    """
    This class represents a quantum gate and its associated errors. 
    It provides methods for working with quantum gates and their error channels.
    """
    def __init__(self, n_qubits):
        """
        Initialize the QuantumGate with the given number of qubits.

        :param n_qubits: The number of qubits the gate operates on.
        """
        self.n = n_qubits
        self.rotate_cont_coh_error = [0] * n_qubits
        self.rotate_uncont_coh_error = [0] * n_qubits

    def get_matrix(self):
        """
        Get the matrix representation of the quantum gate.

        :raises NotImplementedError: This method must be implemented in subclasses.
        :return: The matrix representation of the quantum gate.
        """
        raise NotImplementedError

    def apply_channel_in_ls(self, error_channel):
        """
        Apply an error channel to the quantum gate's Liouville matrix. 
        This method should be implemented to specify how to apply an error channel to the gate's Liouville matrix.

        :param error_channel: The error channel to be applied.
        """
        return

    def get_liouville_matrix(self):
        """
        Get the Liouville matrix representation of the quantum gate.

        :return: The Liouville matrix representation of the quantum gate.
        """
        return Utilities.make_liouville(self.get_matrix())

    def set_rotation_as_coherent_error(self, rotate_cont_coh_error, rotate_uncont_coh_error):
        """
        Set the values of controllable and uncontrollable coherent errors for each qubit.

        :param rotate_cont_coh_error: List of controllable coherent errors for each qubit.
        :param rotate_uncont_coh_error: List of uncontrollable coherent errors for each qubit.
        """
        for qubit in range(self.n):
            self.rotate_cont_coh_error[qubit] = rotate_cont_coh_error[qubit]
            self.rotate_uncont_coh_error[qubit] = rotate_uncont_coh_error[qubit]

