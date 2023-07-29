
# Characterizing Coherent Errors in Quantum Fourier Transform 

The main goal of this project is to show by simulation how our protocol quantifies the amount of coherent errors in a quantum circuit.  The contained tutorials were created as a continuation of my master's research to publish as an article.

# The Motivation Examples 
We provide an example using  QFT (Quantum Fourier Transform). A coherent error (controlable and uncontrolable coherent errors) have been added to each CNOT in addtion to the effect of ADC (amplitude damping channel) to each crosse resonance.

## Steps

* Run the following circuit under the  above asumptions

<img width="1168" alt="qft_ _" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/82cc38a4-e661-4b21-914b-54d4b3580365">

* Apply Randomiesed Compiling (RC) to each CNOT

<img width="1169" alt="rcqft _ _" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/6ec562e2-1044-4861-8227-2e10b56c97c4">


* Applying RC to each  $QFT$ and it's inverse $QFT^{-1}$

  
<img width="1135" alt="qfinvqft" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/1ef21208-3dfb-4295-b984-142f86d05c78">
