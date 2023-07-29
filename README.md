
# Characterizing Coherent Errors in Quantum Fourier Transform 

The main goal of this project is to show by simulation how our protocol quantifies the amount of coherent errors in a quantum circuit.  The contained tutorials were created as a continuation of my master's research to publish as an article.

# The Motivation Examples 
Within tutorials/QFT.py, i have written up motivating examples example using  QFT (Quantum Fourier Transform). A coherent error (controlable and uncontrolable coherent errors) have been added to each CNOT in addtion to the effect of ADC (amplitude damping channel) to each crosse resonance.

## The extraction of coherent errors assosiated with CNOT gate in 4-qubit QFT 

* Simulate the 4-qubit GFT under the above asumptions

  Within this simulation a transformation from Helbert space to Liouville space took place. For further explination look at Ref[1]


<img width="1168" alt="qft_ _" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/82cc38a4-e661-4b21-914b-54d4b3580365">

* Apply Randomiesed Compiling (RC) to each CNOT

  The purpose of this step is to implemnt the KIK method et al. [1,2]. Deonted $QFT^{-1}$ by K and $QFT^{-1}$ by KI, therfore the controlable coherent errors are cancelled and we reman with the uncontrollabel coherent errors.
  
<img width="1135" alt="qfinvqft" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/1ef21208-3dfb-4295-b984-142f86d05c78">


* Applying RC to $QFT$ and it's inverse $QFT^{-1}$

  The implentation that prevent the cancelation of conrollable coherent errors, so it can be detected.
  
<img width="1169" alt="rcqft _ _" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/6ec562e2-1044-4861-8227-2e10b56c97c4">


## Here are the main results.



## References
1- (MAster thesis Mojahed[1](https://www.overleaf.com/read/ctxdfjzkqjnw)])
