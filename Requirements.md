# Requirements for Quantum Computing Practice on macOS

This document outlines the steps and dependencies required to set up your Mac for running quantum computing programs using Qiskit 2.x+.

## 1. Prerequisites
- macOS (darwin 24.3.0 or later)
- Homebrew (recommended for package management)
- Python 3.8 or later

## 2. Setup Steps

### a. Install Homebrew (if not already installed)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### b. Install Python 3 (if not already installed)
```
brew install python
```

### c. Create and Activate a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

### d. Upgrade pip
```
pip install --upgrade pip
```

### e. Install Qiskit and Qiskit Aer
```
pip install qiskit qiskit-aer
```

## 3. Test Your Setup
Create a file named `test_qiskit.py` with the following content:
```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

backend = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, backend)
job = backend.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(compiled_circuit)
print("Measurement results:", counts)
```
Run the test:
```
python test_qiskit.py
```

If you see measurement results, your setup is complete!

## 4. Notes on Qiskit 2.x+
- The `Aer` provider must be imported from `qiskit_aer`, not from `qiskit`.
- The `execute` function is no longer available; use `backend.run()` after transpiling your circuit.
- For more migration details, see the [Qiskit 1.0+ Migration Guide](https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features).

## 5. Additional Resources
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Lab](https://quantum-computing.ibm.com/) 