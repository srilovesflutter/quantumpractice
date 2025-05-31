# Import the QuantumCircuit class for building quantum circuits, and transpile for compiling circuits for a backend
from qiskit import QuantumCircuit, transpile
# Import Aer, the high-performance simulator framework from Qiskit Aer
from qiskit_aer import Aer

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)
# Apply a Hadamard gate to qubit 0, putting it into a superposition state (|0> + |1>)/sqrt(2)
qc.h(0)
# Measure qubit 0 and store the result in classical bit 0
qc.measure(0, 0)

# Select the QASM simulator backend from Aer (simulates quantum circuits by sampling measurement outcomes)
backend = Aer.get_backend('qasm_simulator')
# Transpile (compile/optimize) the circuit for the chosen backend (adapts the circuit to the backend's requirements)
compiled_circuit = transpile(qc, backend)
# Run the compiled circuit on the backend, repeating the experiment 1000 times (shots)
job = backend.run(compiled_circuit, shots=1000)
# Retrieve the results of the simulation (waits for the job to finish and gets the data)
result = job.result()
# Extract the counts of measurement outcomes (e.g., how many times '0' or '1' was measured)
counts = result.get_counts(compiled_circuit)
# Print the measurement results as a dictionary (e.g., {'0': 512, '1': 488})
print("Measurement results:", counts) 