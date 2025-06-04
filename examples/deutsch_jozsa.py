# Deutsch-Jozsa Algorithm Example: Distinguishing Constant vs. Balanced Functions

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Create a quantum circuit with 2 qubits and 1 classical bit
qc = QuantumCircuit(2, 1)

# Step 1: Initialize qubit 1 to |1>
qc.x(1)

# Step 2: Apply Hadamard gates to both qubits
qc.h(0)
qc.h(1)

# Step 3: Oracle for a balanced function (flips the second qubit if the first is 1)
qc.cx(0, 1)

# Step 4: Apply Hadamard to the first qubit again
qc.h(0)

# Step 5: Measure the first qubit
qc.measure(0, 0)

# Select the QASM simulator backend
backend = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, backend)
job = backend.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(compiled_circuit)
print("Measurement results:", counts) 