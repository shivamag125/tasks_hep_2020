# tasks_hep_2020

Task1: 
ML task: file_name: ml_task1.pdf or ml_task.py
Applied ML to solve a High Energy Data analysis issue, more specifically, separating the signal events from the background events.

Imrovement techniques used:
1. Reduced overfitting with dropouts
2. Reduced overfitting by ignoring the last feature column
3. Normalize data

Further improvements:
1. Better hyperparameter(learning rate) search techniques can be employed.
2. Use ensemble of models
3. More data, more features may improve results

Accuracy on training data: 0.8199999928474426
Error on training data: 0.18000000715255737
Accuracy on test data: 0.7400000095367432
Error on test data: 0.25999999046325684


Quantum Computing part:
Task2: file_name=quantum_1.py or quantum_1.pdf
implemented a simple quantum operation with Cirq
1.With 5 qubits
2.Applied Hadamard operation on every qubit
3.Applied CNOT operation on (0, 1), (1,2), (2,3), (3,4)
4.SWAPED (0, 4)
5. Rotated X with pi/2
6. Plotted the circuit


Task 3: file_name=quantum_2.py or quantum_2.pdf
Created a circuit that is a series of small cirq.Rx rotations and plot the probability of measuring the state in the |0⟩ state.


