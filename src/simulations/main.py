from kikCalculation import KikCalculation
from initialState import InitialState
from quantumFourierTransform import QuantumFourierTransform

if __name__ == '__main__':
    # Define the number of qubits to be used in the calculations
    n_qubits = 2
    
    # Instantiate the KikCalculation class:
    # 1. Specify the number of qubits.
    # 2. Generate the initial excited state.
    # 3. Apply the Quantum Fourier Transform.
    kik_obj = KikCalculation(n_qubits, InitialState(n_qubits).generate_excited_state(), QuantumFourierTransform(n_qubits))

    # Plot the comparison between controllable and uncontrollable coherences 
    # versus the effects of Pauli and native errors.
    kik_obj.plot_controllable_and_uncontrollable_coh_vs_pauli_and_native_errors()

    # Uncomment the next line to plot the comparison of Pauli and native errors 
    # against coherence errors.
    # kik_obj.plot_pauli_and_native_vs_coh_errors()
