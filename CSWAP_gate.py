from qiskit import ClassicalRegister,QuantumRegister,QuantumCircuit,Aer
from qiskit.tools.visualization import circuit_drawer
from qiskit import IBMQ
IBMQ.load_account()
S_simulator=Aer.backends(name='statevector_simulator')[0]
M_simulator=Aer.backends(name='qasm_simulator')[0]

q=QuantumRegister(3,name='q')
c=ClassicalRegister(3,name='c')
qc=QuantumCircuit(q,c,name='qc')

qc.iden(q[0])
qc.iden(q[1])
qc.iden(q[2])
qc.cswap(q[0],q[1],q[2])

print(circuit_drawer(qc))