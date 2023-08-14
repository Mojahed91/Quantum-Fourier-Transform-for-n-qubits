import numpy as np
from matplotlib import rcParams
from kikCalculation import KikCalculation
from initialState import InitialState
from quantumFourierTransform import QuantumFourierTransform


rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']

# Constants and Globals
X, Y, Z, I = [np.array([[0, 1], [1, 0]]),
             np.array([[0, -1j], [1j, 0]]),
             np.array([[1, 0], [0, -1]]),
             np.eye(2)]
H = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
I4 = np.kron(I, I)
lr = [[I, I], [I, X], [I, Y], [I, Z], [Y, I], [Y, X], [Y, Y], [Y, Z], [X, I], [X, X], [X, Y], [X, Z], [Z, I], [Z, X], [Z, Y], [Z, Z]]
rr = [[I, I], [I, X], [Z, Y], [Z, Z], [Y, X], [Y, I], [X, Z], [X, Y], [X, X], [X, I], [Y, Z], [Y, Y], [Z, I], [Z, X], [I, Y], [I, Z]]
cnot1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

pauli = [X, Y, Z, I]


if __name__ == '__main__':
    n = 2
    kik_obj = KikCalculation(n, InitialState(n).generate_excited_state(), QuantumFourierTransform(n))

    # kik_obj.plot_controllable_and_uncontrollable_coh_vs_pauli_and_native_errors()
    kik_obj.plot_pauli_and_native_vs_coh_errors()
