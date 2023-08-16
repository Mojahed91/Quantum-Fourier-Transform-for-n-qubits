from kikCalculation import KikCalculation
from initialState import InitialState
from quantumFourierTransform import QuantumFourierTransform

if __name__ == '__main__':
    n_qubits = 2
    kik_obj = KikCalculation(n_qubits, InitialState(n).generate_excited_state(), QuantumFourierTransform(n))

    kik_obj.plot_controllable_and_uncontrollable_coh_vs_pauli_and_native_errors()
    # kik_obj.plot_pauli_and_native_vs_coh_errors()
