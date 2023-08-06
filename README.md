
# Characterizing Coherent Errors in Quantum Fourier Transform 

The main goal of this project is to show by simulation how our protocol quantifies the amount of coherent errors in a quantum circuit.  The contained tutorials were created as a continuation of my master's research to publish as an article.

# The Motivation Examples 
Within tutorials/QFT.py, I have written up motivating example using  QFT (Quantum Fourier Transform). A coherent error (controlable and uncontrolable coherent errors look at Ref[1]) have been added to each CNOT in addtion to the effect of ADC (amplitude damping channel) to each crosse resonance.

## The extraction of coherent errors assosiated with CNOT gate in 4-qubit QFT 

* Simulate the 4-qubit QFT under the above asumptions

  Within this simulation a transformation from Helbert space to Liouville space took place. For further explination look at Ref[1]


<img width="1168" alt="qft_ _" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/82cc38a4-e661-4b21-914b-54d4b3580365">

* Apply Randomiesed Compiling (RC) to each CNOT
  
  The implentation that prevent the cancelation of conrollable coherent errors.
  
  <img width="1167" alt="Screen Shot 2023-08-02 at 10 04 59" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/cf037138-1478-4449-98f4-9882ed9448a6">


* Applying RC to $QFT$ and it's inverse $QFT^{-1}$

  The purpose of this step is to implemnt the KIK method et al. [1,2]. Deonted $QFT^{-1}$ by K and $QFT^{-1}$ by KI, therfore the controlable coherent errors are cancelled and we reman with the uncontrollabel coherent errors.

<img width="1149" alt="Screen Shot 2023-08-02 at 9 33 53" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/d6e50fe7-a822-4cc7-a31f-d75ffa55949d">


## Here are the main results.

* The variation in the error rate p with fixing the coherent error (Controlled and Uncontrolled)

<img width="1218" alt="Screen Shot 2023-08-02 at 0 26 20" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/8b2aa9ab-4aaf-4d42-84ce-b5e177584954">

*  I change the controlled coherent error and mentor the change in the incoherent infidelity with fix error rate

<img width="1222" alt="Screen Shot 2023-08-02 at 10 10 15" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/324ff1ef-7ae4-42c1-8532-f391ee5b5a41">

* Fixing the incoherent error (ADC) and varying the coherent errors (Controlled and Uncontrolled), I mentor the change in the incoherent Pauli and Native error

<img width="1285" alt="res4" src="https://github.com/Mojahed91/QuantumFourierT/assets/129369338/ef8ef38f-ed7e-4dc0-926d-a9dc34a06507">



## References
1- [MAster thesis Mojahed](https://www.overleaf.com/read/ctxdfjzkqjnw)
