
# Characterizing Coherent Errors in Quantum Fourier Transform via Simulation

## Introduction

This project aims to simulate the measurement of coherent errors in a quantum circuit and demonstrate the effectiveness of our protocol. The tutorials included in this repository are a continuation of my master's research and are intended for publication in a research article.

## Motivation and Examples 

In the file simulations/main.py, I have provided an illustrative example using the Quantum Fourier Transform (QFT). I have introduced a coherent error (both controllable and uncontrollable coherent errors, as discussed in Ref[1]) to each CNOT gate. Additionally, the effect of the Amplitude Damping Channel (ADC) has been applied to each cross-resonance.

To see if our approximations hold and provide the desired separation between controlled and uncontrolled coherent errors we validate and demonstrate our findings by simulating qunatum fourier transform (QFT). The way to achieve this is to vary the parameter controlling one type of error and fix the parameters of the other types of errors. The goal is to see that changing the incoherent error, for example, does not affect the coherent errors. In this simulation each CNOT gate is effected by the two types of coherent errors in addition to amplitude damming channel (ADC). We assume a noiseless single qubit gates. 

## Extracting Coherent Errors in n-Qubit Quantum Fourier Transform


By employing CNOT gates, we can successfully carry out the QFT implementation. With 12 CNOT gates involved in the QFT of 4-qubits:
<p align="center">
<img width="750" alt="qft_io" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/e2122986-9241-44a5-8968-fda381cecd26">
<p/>

achieving a high fidelity in the two-qubit gates becomes crucial to observe captivating outcomes. Our initial testing of the protocol involves varying the strength of the amplitude damping channel, with two expected outcomes. Firstly, we must observe a change in incoherent infidelity when measuring the incoherent Pauli error and native error. Secondly, the variation in the amplitude damping channel's strength should not affect coherent errors. Therefore, when measuring the uncontrollable and controllable coherent errors using our protocol, these quantities should remain invariant. In Fig below, we present a simulation of the initial test:
<p align="center">
<img width="450" align="center" style="margin:auto" alt="Screen Shot 2023-08-13 at 11 55 40" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/fd31f755-c99d-4c33-92d9-8b5fb55730af">
<p/>

It's important to observe that the Pauli noise differs from the native noise, even in the absence of coherent errors. This variation occurs due to the influence of RC gates, which modify the profile of the native noise. Consequently, the magnitude of the Pauli noise compared to the native noise can either be greater or lesser, and this behavior is entirely depends on the initial state.


The second test of the protocol involves altering the coherent errors and observing the measured quantities. There are three approaches to conducting this test. The first approach involves fixing the amount of controllable coherent error while varying the uncontrollable coherent errors. The second approach entails a changing function for both controllable and uncontrollable coherent errors. The last approach involves varying both controllable and uncontrollable coherent errors simultaneously. In all three cases, we should expect the following: the measurements of incoherent Pauli errors and native noise should remain the same, as we explained earlier. Additionally, intuitively, we should observe changes in the relevant coherent error throughout the testing process. Our simulation of the second test can be found below:

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
