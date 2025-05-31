# GHZ State Example: Demonstrating Three-Qubit Entanglement with Qiskit
# This script creates a GHZ state (|000> + |111>)/sqrt(2) using three qubits and measures the results.

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Create a quantum circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Step 1: Put qubit 0 into superposition using a Hadamard gate
qc.h(0)
# Step 2: Entangle qubit 0 and qubit 1 using a CNOT gate (control=0, target=1)
qc.cx(0, 1)
# Step 3: Entangle qubit 0 and qubit 2 using another CNOT gate (control=0, target=2)
qc.cx(0, 2)

# Step 4: Measure all qubits and store the results in the classical bits
qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)

# Select the QASM simulator backend
backend = Aer.get_backend('qasm_simulator')
# Transpile the circuit for the backend
compiled_circuit = transpile(qc, backend)
# Run the circuit 1000 times to gather statistics
job = backend.run(compiled_circuit, shots=1000)
# Get the results
result = job.result()
# Get the counts of each measurement outcome (e.g., '000', '111')
counts = result.get_counts(compiled_circuit)
# Print the measurement results
print("Measurement results:", counts) 