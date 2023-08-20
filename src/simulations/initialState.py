
class InitialState:
    """
    Represents the initial state of a quantum system in Liouville space.
    
    Attributes:
        n_qubits (int): The number of qubits in the quantum system.
        size (int): The size of the quantum system's state vector.
    """
    def __init__(self, n_qubits):
        """
        Initializes the InitialState instance with the given number of qubits.
        
        Args:
            n_qubits (int): The number of qubits in the quantum system.
        """
        self.n = n_qubits
        self.size = 2 ** (2 * n_qubits)

    def generate_excited_state(self):
        """
        Generates the excited state of the quantum system.
        
        Returns:
            list: A vector representing the excited state of the quantum system.
        """
        rho_0 = [0] * self.size

        # Set the last element of the list to 1 to represent the excited state
        rho_0[self.size - 1] = 1

        return rho_0

    def generate_ground_state(self):
        """
        Generates the ground state of the quantum system.
        
        Returns:
            list: A vector representing the ground state of the quantum system.
        """
        rho_0 = [0] * self.size

        # Set the first element of the list to 1 to represent the excited state
        rho_0[0] = 1

        return rho_0

