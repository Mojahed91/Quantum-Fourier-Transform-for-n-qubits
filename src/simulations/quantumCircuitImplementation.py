

class QuantumCircuitImplementation:
    """
    Base class for Quantum circuit operations.
    Shared quantum methods or attributes should be placed here.
    """

    def __init__(self, n_qubits):
        self.n_qubits = n_qubits

    def forward_circuit(self):
        raise NotImplementedError("Forward circuit method not implemented.")

    def backward_circuit(self):
        raise NotImplementedError("Backward circuit method not implemented.")

    def forward_circuit_with_rc(self):
        raise NotImplementedError("Forward circuit with RC method not implemented.")

    def backward_circuit_with_rc(self):
        raise NotImplementedError("Backward circuit with RC method not implemented.")

    @property
    def two_qubit_error(self):
        return self.avg_two_qubit_error

    @two_qubit_error.setter
    def two_qubit_error(self, avg_2q_error):
        self.avg_two_qubit_error = avg_2q_error

    @property
    def one_qubit_error(self):
        return self.avg_one_qubit_error

    @one_qubit_error.setter
    def one_qubit_error(self, avg_1q_error):
        self.avg_one_qubit_error = avg_1q_error

