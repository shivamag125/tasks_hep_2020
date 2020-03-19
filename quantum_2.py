import cirq
import numpy as np
from cirq import Circuit
from cirq.devices import GridQubit
from cirq import Simulator
from matplotlib import pyplot as plt

simulator = Simulator()
qbit = cirq.GridQubit(0,0)
circuit = cirq.Circuit()
x = np.arange(0.1,6.2,0.1)
for i in x:
	rot = cirq.rx(i) #rotate by small values,  e^(-i*x/2) phase shift
	circuit.append(rot(qbit))
	# print(i)

print(circuit)
li = []
x = []
for i, step in enumerate(simulator.simulate_moment_steps(circuit)):
    print(np.power(np.abs(step.state_vector()[0]), 2)+np.power(np.abs(step.state_vector()[1]), 2)) #|a|^2 + |b|^2 =1 always(sanity check)
    li.append(np.power(np.abs(step.state_vector()[0]), 2))
    x.append(i*0.1)

plt.plot(x,li)
plt.xlabel("rotation(rads)")
plt.ylabel("probability of |0> state")
#probability of |0> is given by |a|^2
plt.show()