
class InitialState:
    def __init__(self, n_qubits):
        self.n = n_qubits
        self.size = 2 ** (2 * n_qubits)

    def generate_excited_state(self):
        rho_0 = [0] * self.size

        # Set the last element of the list to 1 to represent the excited state
        rho_0[self.size - 1] = 1

        return rho_0

    def generate_ground_state(self):
        rho_0 = [0] * self.size

        # Set the first element of the list to 1 to represent the excited state
        rho_0[0] = 1

        return rho_0

