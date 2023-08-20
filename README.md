
# Characterizing Coherent Errors in Quantum Fourier Transform via Simulation

## Introduction

This project aims to simulate the measurement of coherent errors in a quantum circuit and demonstrate the effectiveness of our protocol. The tutorials included in this repository are a continuation of my master's research and are intended for publication in a research article.

## Motivation and Examples 

The simulations are implemented in the simulations/main.py file. As an illustrative example, we use the Quantum Fourier Transform (QFT) and introduce coherent errors (both controllable and uncontrollable, as discussed in Ref[1]) into each CNOT gate. Furthermore, the effect of the Amplitude Damping Channel (ADC) has been applied to each cross-resonance.

Our approach to validating our findings involves simulating the Quantum Fourier Transform (QFT) and examining the interplay between different types of errors. Specifically, we vary the parameters controlling one type of error while keeping the parameters of other error types fixed. This method allows us to verify that, for example, changing incoherent errors does not impact coherent errors. In these simulations, each CNOT gate is affected by two types of coherent errors as well as the amplitude damping channel (ADC), with single qubit gates assumed to be noiseless.

## Extracting Coherent Errors in n-Qubit Quantum Fourier Transform


By employing CNOT gates, we can successfully carry out the QFT implementation. With 12 CNOT gates involved in the QFT of 4-qubits:
<p align="center">
<img width="750" alt="qft_io" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/e2122986-9241-44a5-8968-fda381cecd26">
<p/>

The QFT can be implemented using CNOT gates. In a 4-qubit QFT, a total of 12 CNOT gates are involved, making high-fidelity two-qubit gates essential for observing interesting results. Our initial protocol testing involves varying the strength of the amplitude damping channel, with two expected outcomes. First, we should observe a change in incoherent infidelity when measuring incoherent Pauli error and native error. Second, changes in the amplitude damping channel's strength should not affect coherent errors, so measurements of uncontrollable and controllable coherent errors should remain consistent. In the Fig below, we present a simulation of the initial test:
<p align="center">
<img width="450" align="center" style="margin:auto" alt="Screen Shot 2023-08-13 at 11 55 40" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/fd31f755-c99d-4c33-92d9-8b5fb55730af">
<p/>

It is crucial to note that Pauli noise differs from native noise even in the absence of coherent errors. This difference arises from the influence of RC gates, which modify the native noise profile. As a result, the magnitude of the Pauli noise compared to the native noise can either be greater or lesser, depending on the initial state.


In the second protocol test, we alter coherent errors and observe the measured quantities. We employ three testing approaches: (1) fixing the controllable coherent error and varying the uncontrollable coherent errors, (2) employing a changing function for both controllable and uncontrollable coherent errors, and (3) varying both types of coherent errors simultaneously. In all cases, we expect the measurements of incoherent Pauli errors and native noise to remain consistent. Additionally, we anticipate observing changes in the relevant coherent error throughout the testing process. Our simulation of the second test illustrated below,

<p align="center">
  <img width="450" alt="res4" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/ef8ef38f-ed7e-4dc0-926d-a9dc34a06507" margin:auto/>
</p>


In Fig below, we illustrate the process of applying an RC gate to a single $QFT$ circuit, 
<p align="center">

  <img width="750" alt="Screen Shot 2023-08-02 at 10 04 59" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/cf037138-1478-4449-98f4-9882ed9448a6">

<p/>
while in here, we demonstrate the effect of the RC gate on the composition $QFT^{-1}QFT$.
<p align="center">

  <img width="750" alt="Screen Shot 2023-08-02 at 9 33 53" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/d6e50fe7-a822-4cc7-a31f-d75ffa55949d">
<p/>

# Characterizing Coherent Errors in IBM Quito backend and lagos backend


The starting point of the investigation of the amount of coherent error and incoherent error on IBM quantum computer is by implementing Pulse inverse technique.

<p align="center">
<img width="750" alt="plcnot" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/8f8cd236-f996-4426-8985-c43d7e22013b">
<p/>

Next, we create the circuits as depicted in the following figures, where we substitute the "k" with a CNOT gate and "k_i" with the inverse of a CNOT gate, implemented through a pulse inversion. We used six cycles.


<p align="center">

<img width="1138" alt="kik_cyc" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/c9f7644d-0901-4f2d-8977-41c67d597a94">
<p/>

<p align="center">

<img width="1261" alt="rckik" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/02b73034-0d7d-4bce-8917-2b462a67fa8c">
<p/>

## Here are the main results of the experimental implementation
<p align="center">

<img width="1142" alt="ert" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/e516c662-1988-40f8-9fef-a464f4dd77eb">
<p/>

## References
1- [Master thesis Mojahed](https://www.overleaf.com/read/ctxdfjzkqjnw)
