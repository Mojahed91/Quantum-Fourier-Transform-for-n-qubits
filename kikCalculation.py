import numpy as np
from sympy import factorial
from iDGate import IDGate
import matplotlib.pyplot as plt
import matplotlib.ticker as tck


# Color parameters
COLOR = ['firebrick', 'royalblue', 'goldenrod', 'cadetblue', 'indigo']
COLOR = ['firebrick', 'royalblue', 'goldenrod', 'goldenrod', 'indigo']
MARKER_SIZE = 26
LINE_STYLE = 'solid'
LINE_WIDTH = 3


class KikCalculation:
    """
    A class to represent a quantum circuit for calculating Four types of errors
    total coherent errors (controllable and uncontrollable) and incoherent Pauli errors and native error.
    """

    def __init__(self, n, rho_0, obj_quantum_cir):
        """
        Initializes a new instance of the QuantumCircuit class.

        :param n: Number of qubits.
        :param rho_0: Initial state.
        :param obj_quantum_cir: The quantum circuit implementation object.
        """
        self.n = n
        self.rho_0 = rho_0
        self.obj_quantum_cir = obj_quantum_cir

    def co_(self, n, k):
        """Compute coefficients for the series expansion."""
        if k == 0:
            return 2 - (1 / n)
        else:
            g = (-1) ** k * (2 * (2 * n - 1) / n) * (factorial(n) ** 2) / (factorial(n - k) * factorial(n + k))
            return float(g)

    # list_sp : list of survival of probabilities
    # order : order of incoherent infidelity
    def incoherent_infidelity(self, order, list_sp):
        """Compute series expansion of the order specified for calculating the incoherent infidelity using Raam Uzdin method.
            For further explanation look at the article "Scalable evaluation of incoherent infidelity in quantum devices"
        """
        if len(list_sp) < order + 1:
            raise ValueError("list_sp doesn't have enough values for the given order")

        inc_inf = sum(self.co_(order, i) * list_sp[i] for i in range(order + 1))
        return inc_inf

    def pauli_and_total_coh_error(self):
        """
        Calculate incoherent infidelity containing information about total coherent error and incoherent Pauli error.
        """
        combined_rc = np.dot(self.obj_quantum_cir.backward_circuit_with_rc(), self.obj_quantum_cir.forward_circuit_with_rc())
        squared_combined_rc = np.dot(combined_rc, combined_rc)
        rho_1 = np.dot(combined_rc, self.rho_0)
        rho_2 = np.dot(squared_combined_rc, self.rho_0)
        return self.incoherent_infidelity(2, [np.dot(self.rho_0, self.rho_0), np.dot(self.rho_0, rho_1), np.dot(self.rho_0, rho_2)])

    def pauli_and_unc_coh_error(self):
        """
        Calculate incoherent infidelity containing information about uncontrollable coherent errors and incoherent Pauli error.
        """
        combined = np.dot(self.obj_quantum_cir.backward_circuit(), self.obj_quantum_cir.forward_circuit())
        rc_uiu = IDGate(self.n).run_pauli_combinations(combined)
        squared_rc_uiu = np.dot(rc_uiu, rc_uiu)
        rho_1 = np.dot(rc_uiu, self.rho_0)
        rho_2 = np.dot(squared_rc_uiu, self.rho_0)
        return self.incoherent_infidelity(2, [np.dot(self.rho_0, self.rho_0), np.dot(self.rho_0, rho_1), np.dot(self.rho_0, rho_2)])

    def pauli_error(self):
        """
        Calculate the incoherent infidelity containing information about incoherent Pauli error only.
        """
        combined = np.dot(self.obj_quantum_cir.backward_circuit(), self.obj_quantum_cir.forward_circuit())
        squared_combined = np.dot(combined, combined)

        rc_uiu = IDGate(self.n).run_pauli_combinations(combined)
        squared_rc_uiu = IDGate(self.n).run_pauli_combinations(squared_combined)

        rho_1 = np.dot(rc_uiu, self.rho_0)
        rho_2 = np.dot(squared_rc_uiu, self.rho_0)

        return self.incoherent_infidelity(2, [np.dot(self.rho_0, self.rho_0), np.dot(self.rho_0, rho_1), np.dot(self.rho_0, rho_2)])

    def native_error(self):
        """
        Calculate the incoherent infidelity of the native noise.
        """
        combined = np.dot(self.obj_quantum_cir.backward_circuit(), self.obj_quantum_cir.forward_circuit())
        squared_combined = np.dot(combined, combined)

        rho_1 = np.dot(combined, self.rho_0)
        rho_2 = np.dot(squared_combined, self.rho_0)

        return self.incoherent_infidelity(2, [np.dot(self.rho_0, self.rho_0), np.dot(self.rho_0, rho_1), np.dot(self.rho_0, rho_2)])

    def calculate_values_of_all_errors(self, snA1, snA2, snA3, snA4):
        A1 = self.pauli_and_total_coh_error()
        A2 = self.pauli_and_unc_coh_error()
        A3 = self.pauli_error()
        A4 = self.native_error()

        snA1.append(A1 - (A3 / 2) - (A2 / 2))
        snA2.append((A2 - A3) / 2)
        snA3.append(A3)
        snA4.append(A4)

        return snA1, snA2, snA3, snA4

    def plot_controllable_and_uncontrollable_coh_vs_pauli_and_native_errors(self):
        """
        Plot the relation between strength of coherent errors and incoherent infidelity.
        In this case the strength of p of ADC is constant.
        """
        f, ax = plt.subplots(figsize=(10, 5))
        print(self.obj_quantum_cir.two_qubit_error)
        max_ang = self.obj_quantum_cir.uncontrollable_coh_err_cx * np.pi
        A_x = np.linspace(0, max_ang, 20)

        snA1, snA2, snA3, snA4, snAa1, snAa2 = [], [], [], [], [], []

        for a in A_x:

            self.obj_quantum_cir.controllable_coh_err_cx = pow(max_ang - a, 1)
            self.obj_quantum_cir.uncontrollable_coh_err_cx = a

            A1 = self.pauli_and_total_coh_error()
            A2 = self.pauli_and_unc_coh_error()

            snA1, snA2, snA3, snA4 = self.calculate_values_of_all_errors(snA1, snA2, snA3, snA4)

            snAa1.append(A1)
            snAa2.append(A2)

        ax.plot(A_x / np.pi, snA1,
                label="Controlled CoError (" + r"$\theta_A$=" + str(max_ang/np.pi) + r"$\pi$-" + r"$\theta_B$)", color=COLOR[1],
                markersize=MARKER_SIZE, linestyle=LINE_STYLE, linewidth=LINE_WIDTH)
        ax.plot(A_x / np.pi, snA2, label="Uncontrolled CoError (" + r"$\theta_B$)", color=COLOR[0], markersize=MARKER_SIZE,
                linestyle=LINE_STYLE, linewidth=LINE_WIDTH)
        ax.plot(A_x / np.pi, snA3, label="Pauli noise", color=COLOR[2], markersize=MARKER_SIZE, linestyle='dashdot', linewidth=LINE_WIDTH)
        ax.plot(A_x / np.pi, snA4, label="Native noise" + "($p_{adc} = $" + str(self.obj_quantum_cir.two_qubit_error) + ")", color=COLOR[3], markersize=MARKER_SIZE,
                linestyle=LINE_STYLE, linewidth=LINE_WIDTH)

        ax.fill_between(A_x / np.pi, np.real(np.array(snA4, dtype=float)), np.real(np.array(snA3, dtype=float)),
                        facecolor='goldenrod', edgecolor='black', alpha=0.02)

        ax.set_ylim(-0.01, 0.07)

        plt.xlabel("Uncontrolled coherent error " + r'$[\theta_B]$', fontsize=30)
        ax.tick_params(axis='x', labelsize=28)
        ax.tick_params(axis='y', labelsize=28)
        plt.ylabel('Incoherent infidelity', fontsize=30, fontweight='ultralight')

        plt.locator_params(nbins=6)
        ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))

        plt.legend(loc="upper left", prop={'weight': 'ultralight', "size": 20})
        plt.show()

    def plot_pauli_and_native_vs_coh_errors(self):

        f, ax = plt.subplots(figsize=(10, 5))
        p_adc = np.linspace(0, self.obj_quantum_cir.two_qubit_error, 20)

        snA1, snA2, snA3, snA4 = [], [], [], []

        for p_ in p_adc:
            self.obj_quantum_cir.two_qubit_error = p_
            snA1, snA2, snA3, snA4 = self.calculate_values_of_all_errors(snA1, snA2, snA3, snA4)

        ax.plot(p_adc, snA1, label="Controlled CoError(" + r"$\theta_A$) = " + str(np.round(self.obj_quantum_cir.controllable_coh_err_cx/np.pi, 3)) + "$\pi$",
                color=COLOR[1], markersize=28, linestyle='solid', linewidth=3)
        ax.plot(p_adc, snA2, label="Uncontrolled CoError(" + r"$\theta_B$) = " + str(np.round(self.obj_quantum_cir.uncontrollable_coh_err_cx/np.pi, 3)) + "$\pi$",
                color=COLOR[0], markersize=28, linestyle='solid', linewidth=3)

        ax.plot(p_adc, snA3, label="Pauli noise", color=COLOR[2], markersize=MARKER_SIZE, linestyle='dashdot', linewidth=LINE_WIDTH)
        ax.plot(p_adc, snA4, label="Native noise", color=COLOR[2], markersize=MARKER_SIZE, linestyle=LINE_STYLE, linewidth=LINE_WIDTH)

        ax.fill_between(p_adc, np.real(np.array(snA3, dtype=float)), np.real(np.array(snA4, dtype=float)), facecolor='goldenrod',
                        edgecolor='black', alpha=0.02)

        ax.set_xlabel('Strength p of ADC', fontsize=30)
        ax.set_ylabel('Incoherent infidelity', fontsize=30, fontweight='ultralight')
        ax.tick_params(axis='x', labelsize=28)
        ax.tick_params(axis='y', labelsize=28)
        ax.locator_params(nbins=6)
        ax.legend(loc="upper left", prop={'weight': 'ultralight', "size": 20})

        plt.show()

